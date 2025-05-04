// src/components/Photos/Photos.tsx
import React from 'react';
import SpaceGallery from './SpaceGallery';

const Photos: React.FC = () => {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-white mb-6">Photo Gallery</h1>
      <SpaceGallery />
    </div>
  );
};

export default Photos;
