import { Phone, Mail, MapPin, Facebook, Instagram, Twitter } from 'lucide-react'
import Logo from './Logo'

const Footer = () => {
  return (
    <footer className="bg-primary-900 text-white">
      <div className="max-w-7xl mx-auto section-padding py-16">
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Company Info */}
          <div className="lg:col-span-2">
            <div className="mb-6">
              <Logo size="md" variant="dark" />
            </div>
            <p className="text-red-100 leading-relaxed mb-6 max-w-md">
              Your trusted partner for premium quality livestock. We specialize in raising 
              healthy, well-cared-for pigs with complete health records and quality guarantee.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="w-10 h-10 bg-primary-800 rounded-full flex items-center justify-center hover:bg-secondary-600 transition-colors duration-200">
                <Facebook className="w-5 h-5" />
              </a>
              <a href="#" className="w-10 h-10 bg-primary-800 rounded-full flex items-center justify-center hover:bg-secondary-600 transition-colors duration-200">
                <Instagram className="w-5 h-5" />
              </a>
              <a href="#" className="w-10 h-10 bg-primary-800 rounded-full flex items-center justify-center hover:bg-secondary-600 transition-colors duration-200">
                <Twitter className="w-5 h-5" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-semibold mb-6">Quick Links</h4>
            <ul className="space-y-3">
              <li><a href="#home" className="text-red-200 hover:text-white transition-colors duration-200">Home</a></li>
              <li><a href="#about" className="text-red-200 hover:text-white transition-colors duration-200">About Us</a></li>
              <li><a href="#animals" className="text-red-200 hover:text-white transition-colors duration-200">Our Animals</a></li>
              <li><a href="#contact" className="text-red-200 hover:text-white transition-colors duration-200">Contact</a></li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h4 className="text-lg font-semibold mb-6">Contact Info</h4>
            <ul className="space-y-4">
              <li className="flex items-start space-x-3">
                <Phone className="w-5 h-5 text-secondary-400 mt-0.5" />
                <div>
                  <p className="text-red-200">+234 123 456 7890</p>
                  <p className="text-red-200">+234 987 654 3210</p>
                </div>
              </li>
              <li className="flex items-start space-x-3">
                <Mail className="w-5 h-5 text-secondary-400 mt-0.5" />
                <div>
                  <p className="text-red-200">info@ade-hi.com</p>
                  <p className="text-red-200">sales@ade-hi.com</p>
                </div>
              </li>
              <li className="flex items-start space-x-3">
                <MapPin className="w-5 h-5 text-secondary-400 mt-0.5" />
                <p className="text-red-200">Lagos State, Nigeria</p>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-primary-800 mt-12 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-red-200 text-sm">
              © 2024 ADE-HI Integrated Farm Limited. All rights reserved.
            </p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="text-red-200 hover:text-white text-sm transition-colors duration-200">Privacy Policy</a>
              <a href="#" className="text-red-200 hover:text-white text-sm transition-colors duration-200">Terms of Service</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer