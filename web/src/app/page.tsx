'use client'

import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import ChatUI, { Message } from './chat';

export function Card({ content }: { content: string }) {
  return (
    <div className="rounded-lg border w-full min-h-32 p-6 dark:prose-invert prose lg:prose-xl">
      <ReactMarkdown
        children={content}
      />
    </div>
  );
}

export default function Home() {
  const [contents, setContents] = useState<string[]>([]);
  const [messages, setMessages] = useState<Message[]>([])

  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://localhost:5000/get-event')
        .then(response => response.json())
        .then((data: string[]) => {
          // Filter out data that's already in the contents list
          const newData = data.filter(content => !contents.includes(content));

          // Update contents with the new, non-duplicate data
          setContents(prev => [...prev, ...newData]);

          // Create a list of messages from the new data
          const _messages: Message[] = newData.map(content => ({
            role: "assistant",
            content: content,
          }));

          if (_messages.length > 0) {
            setMessages(prevMessages => [...prevMessages, ..._messages]);
          }
          // Update messages state
        })
        .catch(error => console.error('Error fetching data:', error));
    }, 2000);

    return () => clearInterval(interval); // Clean up the interval on component unmount
  }, [contents]); // Add `contents` to the dependency array to ensure the effect uses the latest state


  return (
    <main className="flex min-h-screen flex-col items-center">
      <header className="my-6 text-2xl font-bold">Harsh Assistant Built with P.A.L</header>
      <div className="w-full max-w-5xl flex flex-wrap justify-center space-y-4 h-[calc(100vh-100px)]">
        <ChatUI 
          onSubmit={(text) => console.log(text)}
          messages={messages}
          isGenerating={false}
        />
      </div>
    </main>
  );
}
