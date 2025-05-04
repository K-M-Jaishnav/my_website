import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Mail, MapPin, Phone, Clock, Send, Twitter, Linkedin, Github } from 'lucide-react';

const Contact = () => {
  const [formState, setFormState] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormState(prev => ({ ...prev, [name]: value }));
  };
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Form submitted:', formState);
    // Here you would typically send the form data to a server
    alert('Thank you for your message! I will get back to you soon.');
    setFormState({
      name: '',
      email: '',
      subject: '',
      message: ''
    });
  };
  
  return (
    <>
      {/* Hero Section */}
      <section className="pt-32 pb-20 bg-gradient-to-b from-space-navy to-space-dark text-white">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="mb-6">Get in Touch</h1>
            <p className="text-xl text-gray-300">
              Have a question or want to collaborate? Feel free to reach out.
            </p>
          </div>
        </div>
      </section>
      
      {/* Contact Section */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div className="lg:col-span-1">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.8 }}
              >
                <h2 className="text-space-dark mb-6">Contact Information</h2>
                <p className="text-gray-700 mb-8">
                  Feel free to contact me with any questions or inquiries. 
                  I'm available for consulting, speaking engagements, and research collaborations.
                </p>
                
                <div className="space-y-6">
                  <div className="flex items-start">
                    <MapPin className="w-6 h-6 text-space-accent mr-4 mt-1" />
                    <div>
                      <h3 className="font-bold mb-1">Address</h3>
                      <address className="not-italic text-gray-600">
                        University of Aerospace<br />
                        1234 Flight Boulevard<br />
                        Aviation City, AC 10101
                      </address>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <Mail className="w-6 h-6 text-space-accent mr-4 mt-1" />
                    <div>
                      <h3 className="font-bold mb-1">Email</h3>
                      <a href="mailto:contact@example.com" className="text-gray-600 hover:text-space-accent transition-colors">
                        contact@example.com
                      </a>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <Phone className="w-6 h-6 text-space-accent mr-4 mt-1" />
                    <div>
                      <h3 className="font-bold mb-1">Phone</h3>
                      <a href="tel:+1234567890" className="text-gray-600 hover:text-space-accent transition-colors">
                        (123) 456-7890
                      </a>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <Clock className="w-6 h-6 text-space-accent mr-4 mt-1" />
                    <div>
                      <h3 className="font-bold mb-1">Office Hours</h3>
                      <p className="text-gray-600">
                        Monday - Friday: 9:00 AM - 5:00 PM<br />
                        Saturday: By appointment<br />
                        Sunday: Closed
                      </p>
                    </div>
                  </div>
                </div>
                
                <div className="mt-8">
                  <h3 className="font-bold mb-3">Connect With Me</h3>
                  <div className="flex space-x-4">
                    <a href="#" aria-label="Twitter" className="bg-space-light hover:bg-space-accent hover:text-white transition-all p-3 rounded-full">
                      <Twitter className="w-5 h-5" />
                    </a>
                    <a href="#" aria-label="LinkedIn" className="bg-space-light hover:bg-space-accent hover:text-white transition-all p-3 rounded-full">
                      <Linkedin className="w-5 h-5" />
                    </a>
                    <a href="#" aria-label="Github" className="bg-space-light hover:bg-space-accent hover:text-white transition-all p-3 rounded-full">
                      <Github className="w-5 h-5" />
                    </a>
                  </div>
                </div>
              </motion.div>
            </div>
            
            <motion.div 
              className="lg:col-span-2"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8, delay: 0.2 }}
            >
              <div className="bg-space-light p-8 rounded-lg">
                <h2 className="text-space-dark mb-6">Send Me a Message</h2>
                <form onSubmit={handleSubmit}>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                      <label htmlFor="name" className="block text-gray-700 font-medium mb-2">Your Name</label>
                      <input
                        type="text"
                        id="name"
                        name="name"
                        value={formState.name}
                        onChange={handleChange}
                        required
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-space-dark"
                        placeholder="John Doe"
                      />
                    </div>
                    <div>
                      <label htmlFor="email" className="block text-gray-700 font-medium mb-2">Your Email</label>
                      <input
                        type="email"
                        id="email"
                        name="email"
                        value={formState.email}
                        onChange={handleChange}
                        required
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-space-dark"
                        placeholder="john@example.com"
                      />
                    </div>
                  </div>
                  
                  <div className="mb-6">
                    <label htmlFor="subject" className="block text-gray-700 font-medium mb-2">Subject</label>
                    <select
                      id="subject"
                      name="subject"
                      value={formState.subject}
                      onChange={handleChange}
                      required
                      className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-space-dark"
                    >
                      <option value="">Select a subject</option>
                      <option value="Research Inquiry">Research Inquiry</option>
                      <option value="Book Question">Book Question</option>
                      <option value="Speaking Engagement">Speaking Engagement</option>
                      <option value="Collaboration">Collaboration</option>
                      <option value="Other">Other</option>
                    </select>
                  </div>
                  
                  <div className="mb-6">
                    <label htmlFor="message" className="block text-gray-700 font-medium mb-2">Your Message</label>
                    <textarea
                      id="message"
                      name="message"
                      value={formState.message}
                      onChange={handleChange}
                      required
                      className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-space-dark h-32"
                      placeholder="Your message here..."
                    ></textarea>
                  </div>
                  
                  <motion.button
                    type="submit"
                    className="btn-primary flex items-center justify-center"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    Send Message <Send className="ml-2 w-4 h-4" />
                  </motion.button>
                </form>
              </div>
            </motion.div>
          </div>
        </div>
      </section>
      
      {/* Map Section */}
      <section className="py-16 bg-space-light">
        <div className="container-custom">
          <h2 className="text-space-dark text-center mb-8">Find Me</h2>
          <div className="aspect-w-16 aspect-h-9 bg-white rounded-lg shadow-md overflow-hidden h-96">
            {/* This would typically be a map embed */}
            <div className="w-full h-full bg-gray-200 flex items-center justify-center">
              <p className="text-gray-600 text-lg">Interactive Map Would Be Displayed Here</p>
            </div>
          </div>
        </div>
      </section>
      
      {/* FAQ Section */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <h2 className="text-space-dark text-center mb-10">Frequently Asked Questions</h2>
          <div className="max-w-3xl mx-auto">
            <div className="space-y-6">
              <div className="border-b border-gray-200 pb-4">
                <h3 className="text-xl font-bold mb-2">Are you available for consulting?</h3>
                <p className="text-gray-600">
                  Yes, I offer consulting services for aerospace companies, research institutions, 
                  and educational organizations. Please contact me with details about your project 
                  for availability and rates.
                </p>
              </div>
              
              <div className="border-b border-gray-200 pb-4">
                <h3 className="text-xl font-bold mb-2">Do you offer speaking engagements?</h3>
                <p className="text-gray-600">
                  I regularly speak at conferences, universities, and industry events on topics 
                  related to aerospace engineering, aerodynamics, and computational methods. 
                  Contact me with your event details for availability.
                </p>
              </div>
              
              <div className="border-b border-gray-200 pb-4">
                <h3 className="text-xl font-bold mb-2">How can I get a signed copy of your books?</h3>
                <p className="text-gray-600">
                  You can request a signed copy by contacting me directly. Please include your 
                  shipping information and which book(s) you're interested in, and I'll provide 
                  details about payment and shipping.
                </p>
              </div>
              
              <div className="border-b border-gray-200 pb-4">
                <h3 className="text-xl font-bold mb-2">Do you take on graduate students?</h3>
                <p className="text-gray-600">
                  I currently supervise a limited number of graduate students at the University 
                  of Aerospace. Prospective students should apply through the university's 
                  regular admission process and mention my name as a potential advisor.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Contact;
