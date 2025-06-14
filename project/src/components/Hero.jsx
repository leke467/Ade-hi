import { ArrowRight, Star, Users, Award } from 'lucide-react'

const Hero = () => {
  return (
    <section id="home" className="bg-gradient-to-br from-primary-900 via-primary-800 to-primary-600 text-white py-20">
      <div className="max-w-7xl mx-auto section-padding">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Content */}
          <div className="space-y-8">
            <div className="space-y-4">
              <h1 className="text-4xl lg:text-6xl font-bold leading-tight">
                Premium Quality
                <span className="text-secondary-400 block">Livestock</span>
                for Your Needs
              </h1>
              <p className="text-xl text-red-100 max-w-lg leading-relaxed">
                ADE-HI Integrated Farm Limited is your trusted partner for high-quality pigs and livestock. 
                We specialize in raising healthy, well-cared-for animals with complete health records.
              </p>
            </div>

            {/* Stats */}
            <div className="grid grid-cols-3 gap-6">
              <div className="text-center">
                <div className="flex items-center justify-center w-12 h-12 bg-secondary-500 rounded-full mx-auto mb-2">
                  <Users className="w-6 h-6" />
                </div>
                <div className="text-2xl font-bold">500+</div>
                <div className="text-sm text-red-200">Happy Customers</div>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center w-12 h-12 bg-secondary-500 rounded-full mx-auto mb-2">
                  <Award className="w-6 h-6" />
                </div>
                <div className="text-2xl font-bold">10+</div>
                <div className="text-sm text-red-200">Years Experience</div>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center w-12 h-12 bg-secondary-500 rounded-full mx-auto mb-2">
                  <Star className="w-6 h-6" />
                </div>
                <div className="text-2xl font-bold">5.0</div>
                <div className="text-sm text-red-200">Rating</div>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <a href="#animals" className="btn-secondary inline-flex items-center justify-center">
                View Our Animals
                <ArrowRight className="ml-2 w-5 h-5" />
              </a>
              <a href="#contact" className="border-2 border-white text-white hover:bg-white hover:text-primary-600 px-6 py-3 rounded-lg font-medium transition-all duration-200 text-center">
                Contact Us
              </a>
            </div>
          </div>

          {/* Image */}
          <div className="relative">
            <div className="aspect-square rounded-2xl overflow-hidden bg-gradient-to-br from-secondary-400 to-secondary-600 p-1">
              <img
                src="https://images.pexels.com/photos/1300355/pexels-photo-1300355.jpeg?auto=compress&cs=tinysrgb&w=800"
                alt="Happy pigs at ADE-HI Farm"
                className="w-full h-full object-cover rounded-xl"
              />
            </div>
            {/* Floating Card */}
            <div className="absolute -bottom-6 -left-6 bg-white text-gray-900 p-6 rounded-xl shadow-xl">
              <div className="flex items-center space-x-3">
                <div className="w-12 h-12 bg-secondary-100 rounded-full flex items-center justify-center">
                  <Star className="w-6 h-6 text-secondary-600 fill-current" />
                </div>
                <div>
                  <div className="text-lg font-bold">Premium Quality</div>
                  <div className="text-sm text-gray-600">Certified & Healthy</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Hero