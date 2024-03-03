'use client'

import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';

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

  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://localhost:5000/get-event')
        .then(response => response.json()) // Assuming the API returns plain text
        .then(data => {
          console.log(data)
          setContents(data);
        })
        .catch(error => console.error('Error fetching data:', error));
    }, 2000);

    return () => clearInterval(interval); // Clean up the interval on component unmount
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <header className="my-6 text-2xl font-bold">P.A.L - Proactive Agent Library</header>
      <div className="w-full max-w-5xl flex flex-wrap justify-center space-y-4">
        {contents.map((content, index) => (
          <Card key={index} content={content} />
        ))}
      </div>
    </main>
  );
}
