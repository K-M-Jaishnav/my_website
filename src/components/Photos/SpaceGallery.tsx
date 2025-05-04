// src/components/Photos/SpaceGallery.tsx
import React from 'react';

const SpaceGallery: React.FC = () => {
  const personalities = [
    { image: '/images/1.jpg' },
    { image: '/images/2.jpg' },
    { image: '/images/3.jpg' },
    { image: '/images/4.jpg' },
    { image: '/images/5.jpg' }
  ];

  return (
    <section className="mt-8">
      <h2 className="text-2xl font-semibold text-white mb-4">Top Space Personalities</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
        {personalities.map((person, index) => (
          <div key={index} className="relative">
            <img
              src={person.image}
              alt={`Space personality ${index + 1}`}
              className="w-full h-auto object-cover rounded-lg shadow-lg"
            />
          </div>
        ))}
      </div>
    </section>
  );
};

export default SpaceGallery;
