import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Calendar, Clock, User, Tag, Search } from 'lucide-react';

const articles = [
  {
    id: 1,
    title: "The Future of Supersonic Commercial Flight",
    excerpt: "Exploring how new technologies are making supersonic commercial travel viable once again, with a focus on noise reduction and fuel efficiency improvements.",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum...",
    date: "Apr 15, 2025",
    readTime: "8 min read",
    author: "Dr. John Smith",
    image: "https://images.pexels.com/photos/76964/supersonic-tupolev-tu-144-aircraft-fly-76964.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    categories: ["Aerodynamics", "Commercial Aviation"]
  },
  {
    id: 2,
    title: "Advancements in Computational Fluid Dynamics",
    excerpt: "How modern Python libraries are revolutionizing the way we simulate complex fluid dynamics problems in aerospace applications.",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum...",
    date: "Mar 22, 2025",
    readTime: "12 min read",
    author: "Dr. John Smith",
    image: "https://images.pexels.com/photos/8947554/pexels-photo-8947554.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    categories: ["Computational Methods", "Fluid Dynamics"]
  },
  {
    id: 3,
    title: "Sustainable Aviation: Challenges and Solutions",
    excerpt: "Analyzing the environmental impact of aviation and innovative approaches to sustainability including electric propulsion and advanced materials.",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum...",
    date: "Feb 10, 2025",
    readTime: "10 min read",
    author: "Dr. John Smith",
    image: "https://images.pexels.com/photos/46148/aircraft-jet-landing-cloud-46148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    categories: ["Sustainability", "Future Tech"]
  },
  {
    id: 4,
    title: "The Role of AI in Aircraft Design Optimization",
    excerpt: "How machine learning and artificial intelligence are transforming aircraft design processes, enabling more efficient and innovative solutions.",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum...",
    date: "Jan 28, 2025",
    readTime: "15 min read",
    author: "Dr. John Smith",
    image: "https://images.pexels.com/photos/47044/aircraft-landing-reach-injection-47044.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    categories: ["Artificial Intelligence", "Aircraft Design"]
  },
  {
    id: 5,
    title: "Hypersonic Flight: Technical Challenges",
    excerpt: "An exploration of the technical obstacles facing hypersonic flight including thermal management, materials science, and propulsion systems.",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum...",
    date: "Dec 15, 2024",
    readTime: "11 min read",
    author: "Dr. John Smith",
    image: "https://images.pexels.com/photos/219692/pexels-photo-219692.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    categories: ["Hypersonics", "Propulsion"]
  },
  {
    id: 6,
    title: "Space Tourism: Engineering for Comfort and Safety",
    excerpt: "Examining the unique engineering challenges of designing spacecraft for civilian passengers with a focus on safety, comfort, and accessibility.",
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum...",
    date: "Nov 30, 2024",
    readTime: "9 min read",
    author: "Dr. John Smith",
    image: "https://images.pexels.com/photos/23808/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    categories: ["Space", "Tourism"]
  }
];

const allCategories = [... new Set(articles.flatMap(article => article.categories))];

const Blog = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  
  const filteredArticles = articles.filter(article => {
    const matchesSearch = article.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         article.excerpt.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesCategory = selectedCategory === '' || article.categories.includes(selectedCategory);
    
    return matchesSearch && matchesCategory;
  });
  
  return (
    <>
      {/* Hero Section */}
      <section className="pt-32 pb-20 bg-gradient-to-b from-space-navy to-space-dark text-white">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="mb-6">Blog & Articles</h1>
            <p className="text-xl text-gray-300">
              Insights, research, and thoughts on aerospace engineering, 
              aerophysics, and computational methods.
            </p>
          </div>
        </div>
      </section>
      
      {/* Search and Filter */}
      <section className="py-10 bg-space-light">
        <div className="container-custom">
          <div className="flex flex-col md:flex-row gap-4 md:items-center justify-between">
            <div className="relative md:w-1/3">
              <input
                type="text"
                placeholder="Search articles..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-space-dark"
              />
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
            </div>
            
            <div className="md:w-1/3">
              <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-space-dark"
              >
                <option value="">All Categories</option>
                {allCategories.map((category, index) => (
                  <option key={index} value={category}>{category}</option>
                ))}
              </select>
            </div>
          </div>
        </div>
      </section>
      
      {/* Articles */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          {filteredArticles.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {filteredArticles.map((article, index) => (
                <motion.article 
                  key={article.id}
                  className="bg-white rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-all"
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                >
                  <div className="h-56 overflow-hidden">
                    <img 
                      src={article.image} 
                      alt={article.title} 
                      className="w-full h-full object-cover transition-transform duration-500 hover:scale-105"
                    />
                  </div>
                  <div className="p-6">
                    <div className="flex flex-wrap gap-2 mb-3">
                      {article.categories.map((category, i) => (
                        <span 
                          key={i} 
                          className="bg-space-light text-space-dark text-xs px-2 py-1 rounded-full flex items-center"
                        >
                          <Tag className="w-3 h-3 mr-1" /> {category}
                        </span>
                      ))}
                    </div>
                    
                    <h3 className="text-xl font-bold mb-3 hover:text-space-accent transition-colors">
                      <a href="#">{article.title}</a>
                    </h3>
                    
                    <p className="text-gray-600 mb-4">{article.excerpt}</p>
                    
                    <div className="flex items-center text-sm text-gray-500 mb-4">
                      <span className="flex items-center mr-4">
                        <Calendar className="w-4 h-4 mr-1" /> {article.date}
                      </span>
                      <span className="flex items-center mr-4">
                        <Clock className="w-4 h-4 mr-1" /> {article.readTime}
                      </span>
                      <span className="flex items-center">
                        <User className="w-4 h-4 mr-1" /> {article.author}
                      </span>
                    </div>
                    
                    <a href="#" className="text-space-dark font-medium hover:text-space-accent transition-colors">
                      Read Article →
                    </a>
                  </div>
                </motion.article>
              ))}
            </div>
          ) : (
            <div className="text-center py-16">
              <h3 className="text-2xl font-bold mb-4">No articles found</h3>
              <p className="text-gray-600">Try adjusting your search or filter criteria</p>
            </div>
          )}
        </div>
      </section>
      
      {/* Subscribe Section */}
      <section className="py-16 bg-space-navy text-white">
        <div className="container-custom">
          <div className="max-w-2xl mx-auto text-center">
            <h2 className="mb-6">Subscribe to My Newsletter</h2>
            <p className="text-gray-300 mb-8">
              Get notified when I publish new articles, research papers, or book updates. 
              I send updates approximately once a month.
            </p>
            
            <form className="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto">
              <input
                type="email"
                placeholder="Your email address"
                className="flex-1 px-4 py-3 rounded-md focus:outline-none focus:ring-2 focus:ring-space-accent text-gray-800"
                required
              />
              <button type="submit" className="bg-space-accent hover:bg-opacity-90 text-white py-3 px-6 rounded-md font-medium transition-all duration-300">
                Subscribe
              </button>
            </form>
            <p className="text-sm text-gray-400 mt-4">
              I respect your privacy. Unsubscribe at any time.
            </p>
          </div>
        </div>
      </section>
    </>
  );
};

export default Blog;
