import React from 'react';

function SpaceGallery() {
  // Define an array of space personalities with image paths and captions.
  const personalities = [
    { image: '/1.jpg' },
    { image: '/2.jpg' }
    { image: '3.jpg },
    { image: '/4.jpg },
    { image: '/5.jpg'}
    // Add more entries as needed...
  ];

  return (
    <section className="mt-8">
      <h2 className="text-2xl font-semibold text-white mb-4">Top Space Personalities</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-5">
        {personalities.map((person, index) => (
          <div key={index} className="relative">
            <img
              src={person.image}
              alt={person.name}
              className="w-full h-auto object-cover rounded-lg shadow-lg"
            />
            <p className="absolute bottom-0 left-0 right-0 text-center text-white bg-black bg-opacity-50 py-1">
              {person.name}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default SpaceGallery;
