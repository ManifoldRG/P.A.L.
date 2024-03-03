'use client';

import React, { useState, useMemo, useRef, ReactNode, KeyboardEvent, useEffect } from 'react';
import ReactMarkdown from 'react-markdown'
import { Button } from '../components/ui/button';
import { UserCircleIcon, ArrowDownCircleIcon, ArrowUpCircleIcon } from '@heroicons/react/20/solid';
import { cn } from "../lib/utils"
import { Textarea } from '../components/ui/textarea';
import { ScrollArea } from '../components/ui/scroll-area';
import {
    Avatar,
    AvatarFallback,
    AvatarImage,
} from "../components/ui/avatar"

export interface Message {
    role: 'assistant' | 'user' | 'system';
    content: string;
}

interface FormatterProps {
    content: string;
}

// fix for inline code ts-error
declare module 'react' {
    interface HTMLAttributes<T> extends AriaAttributes, DOMAttributes<T> {
        inline?: boolean;
    }
}

function Formatter({ content }: FormatterProps) {
    return (
        <div className="h-full w-full formatter prose lg:prose-xl">
            <ReactMarkdown
                children={content} // eslint-disable-line react/no-children-prop
            />
        </div>
    )
}

const RefreshIcon = ({ className = "w6 h6" }: { className: string }) => (
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className={className}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
    </svg>
)


const AssistantMessage: React.FC<{ children: ReactNode, avatar: string }> = ({ children, avatar }) => {
    return (
        <div className="p-4 rounded-lg flex">
            <div className="mr-4">
                <Avatar className="h-8 w-8">
                    <AvatarImage className="object-cover" src={avatar} alt="bot" />
                    <AvatarFallback>AI</AvatarFallback>
                </Avatar>
            </div>
            {children}
        </div>
    )
}

const UserMessage: React.FC<{ children: ReactNode }> = ({ children }) => {
    return (
        <div className="p-4 rounded-lg flex">
            <div className="mr-4">
                <UserCircleIcon className="h-8 w-8" />
            </div>
            {children}
        </div>
    )
};

interface ChatProps {
    messages: Message[];
    onSubmit: (messages: Message[]) => void;
    isGenerating: boolean;
    className?: string;
    avatar?: string;
}


const ChatUI: React.FC<ChatProps> = ({
    onSubmit,
    messages,
    isGenerating,
    avatar,
    className = "",
}) => {
    const [input, setInput] = useState<string>('');
    const [isManualScroll, setIsManualScroll] = useState<boolean>(false);

    const scrollAreaRef = useRef<HTMLDivElement>(null);
    const lastChatRef = useRef<HTMLDivElement>(null);
    const textAreaRef = useRef<HTMLTextAreaElement>(null);

    useEffect(() => {
        if (!isGenerating) {
            textAreaRef.current?.focus();
        }
    }, [isGenerating]);

    useEffect(() => {
        if (messages && scrollAreaRef.current && !isManualScroll) {
            const scrollArea = scrollAreaRef.current;
            const top = scrollArea.scrollHeight - scrollArea.clientHeight;
            scrollArea.scrollTop = top;
            setIsManualScroll(false); // Reset the manual scroll state after scrolling
        }
    }, [messages, isManualScroll]);

    const handleSubmit = (e?: React.FormEvent<HTMLFormElement>) => {
        if (e) e.preventDefault();
        if (input.trim()) {
            const updatedMessages: Message[] = [
                ...messages,
                { role: "user", content: input.trim() }
            ]
            onSubmit(updatedMessages);
            setInput('');
        }
    };

    function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
        // Check if 'Enter' key was pressed
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent the default action to avoid inserting a new line
            handleSubmit(); // Call your submit handler
        }
    }

    const handleScroll = (e: React.UIEvent<HTMLDivElement>) => {
        const target = e.currentTarget;
        const atBottom = Math.ceil(target.scrollHeight - target.scrollTop) <= target.clientHeight + 20; // Adding a small tolerance value (+1)
        if (!atBottom) {
            // The user has manually scrolled away from the bottom of the chat
            setIsManualScroll(true);
        } else {
            // The user is at the bottom, you might want to consider this as auto-scroll
            setIsManualScroll(false);
        }
    };

    // scroll to bottom function
    const scrollToBottom = () => {
        if (scrollAreaRef.current) {
            const scrollArea = scrollAreaRef.current;
            const top = scrollArea.scrollHeight - scrollArea.clientHeight;
            scrollArea.scrollTop = top;
        }
    }

    const formatterComponents = useMemo(
        () => {
            return (
                <>
                    {messages.map((message, index) => (
                        message.role === 'user' ? (
                            <div key={index}>
                                <UserMessage>
                                    <Formatter content={message.content} />
                                </UserMessage>
                            </div>
                        ) : (
                            <div key={index} >
                                <AssistantMessage avatar={avatar as string}>
                                    <Formatter content={message.content} />
                                </AssistantMessage>
                            </div>
                        )
                    ))}
                    {isManualScroll && <div className="sticky bottom-5 w-full flex justify-center">
                        <div className="rounded-full bg-black">
                            <ArrowDownCircleIcon onClick={scrollToBottom} className="h-8 cursor-pointer text-muted-foreground" />
                        </div>
                    </div>}
                    <div ref={lastChatRef} className="h-1" />
                </>
            )
        },
        [messages, isManualScroll]
    );

    return (
        <div className={cn("border text-primary flex flex-col p-4 h-full w-full", className)}>
            <div className="w-full flex-grow flex flex-col justify-between h-full">
                <div ref={scrollAreaRef} className={cn("overflow-y-auto border-b flex-grow", className)} onScroll={handleScroll}>
                    {formatterComponents}
                </div>
                <form onSubmit={handleSubmit} className="flex py-4 px-4 items-center">
                    <div className="relative flex-1 ">
                        <Textarea
                            ref={textAreaRef}
                            autoFocus
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={(e) => handleKeyDown(e)}
                            className=" p-4 text-base rounded-lg pr-10 w-full"
                            disabled={isGenerating}
                        />
                    </div>
                    <Button
                        disabled={isGenerating}
                        type="submit"
                        className="bg-background hover:bg-secondary flex items-center justify-center px-4 focus:outline-none"
                    >
                        <ArrowUpCircleIcon className="text-foreground w-6 h-6" />
                    </Button>
                </form>
            </div>
        </div>
    );
};

export default ChatUI;