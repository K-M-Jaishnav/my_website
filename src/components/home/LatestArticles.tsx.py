import React from 'react';
import { motion } from 'framer-motion';
import { Calendar, Clock, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

const articles = [
  {
    id: 1,
    title: "The Future of Supersonic Commercial Flight",
    excerpt: "Exploring how new technologies are making supersonic commercial travel viable once again...",
    date: "Apr 15, 2025",
    readTime: "8 min read",
    image: "https://images.pexels.com/photos/76964/supersonic-tupolev-tu-144-aircraft-fly-76964.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
  {
    id: 2,
    title: "Advancements in Computational Fluid Dynamics",
    excerpt: "How modern Python libraries are revolutionizing the way we simulate complex fluid dynamics...",
    date: "Mar 22, 2025",
    readTime: "12 min read",
    image: "https://images.pexels.com/photos/8947554/pexels-photo-8947554.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
  {
    id: 3,
    title: "Sustainable Aviation: Challenges and Solutions",
    excerpt: "Analyzing the environmental impact of aviation and innovative approaches to sustainability...",
    date: "Feb 10, 2025",
    readTime: "10 min read",
    image: "https://images.pexels.com/photos/46148/aircraft-jet-landing-cloud-46148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  }
];

const LatestArticles = () => {
  return (
    <section className="section bg-space-light">
      <div className="container-custom">
        <div className="text-center mb-12">
          <p className="text-space-accent font-medium mb-2">INSIGHTS & KNOWLEDGE</p>
          <h2 className="text-space-dark mb-4">Latest Articles</h2>
          <p className="max-w-2xl mx-auto text-gray-600">
            Stay updated with my latest research, insights, and thoughts on aerospace 
            engineering, aerophysics, and computational methods.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {articles.map((article, index) => (
            <motion.article 
              key={article.id}
              className="bg-white rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-all"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <div className="h-48 overflow-hidden">
                <img 
                  src={article.image} 
                  alt={article.title} 
                  className="w-full h-full object-cover transition-transform duration-500 hover:scale-105"
                />
              </div>
              <div className="p-6">
                <div className="flex items-center text-sm text-gray-500 mb-3">
                  <span className="flex items-center mr-4">
                    <Calendar className="w-4 h-4 mr-1" /> {article.date}
                  </span>
                  <span className="flex items-center">
                    <Clock className="w-4 h-4 mr-1" /> {article.readTime}
                  </span>
                </div>
                <h3 className="text-xl font-bold mb-3">{article.title}</h3>
                <p className="text-gray-600 mb-4">{article.excerpt}</p>
                <Link to="/blog" className="text-space-dark font-medium inline-flex items-center hover:text-space-accent transition-colors">
                  Read More <ArrowRight className="w-4 h-4 ml-1" />
                </Link>
              </div>
            </motion.article>
          ))}
        </div>
        
        <div className="text-center mt-12">
          <Link to="/blog" className="btn-primary">
            View All Articles
          </Link>
        </div>
      </div>
    </section>
  );
};

export default LatestArticles;
