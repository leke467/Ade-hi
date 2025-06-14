import { Shield, Heart, Truck, Award } from 'lucide-react'

const About = () => {
  const features = [
    {
      icon: Shield,
      title: 'Health Certified',
      description: 'All our animals are regularly checked by certified veterinarians and come with complete health records.'
    },
    {
      icon: Heart,
      title: 'Ethical Care',
      description: 'We prioritize animal welfare with proper nutrition, comfortable housing, and stress-free environments.'
    },
    {
      icon: Truck,
      title: 'Safe Delivery',
      description: 'Professional transportation services ensuring your animals arrive safely and in perfect condition.'
    },
    {
      icon: Award,
      title: 'Quality Guarantee',
      description: 'We stand behind our livestock with quality guarantees and ongoing support for our customers.'
    }
  ]

  return (
    <section id="about" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto section-padding">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Why Choose ADE-HI Farm?
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            We're committed to providing the highest quality livestock with exceptional care standards. 
            Our experience and dedication ensure you get healthy, well-raised animals every time.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
          {features.map((feature, index) => (
            <div key={index} className="text-center group">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-primary-600 transition-colors duration-300">
                <feature.icon className="w-8 h-8 text-primary-600 group-hover:text-white" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">{feature.title}</h3>
              <p className="text-gray-600 leading-relaxed">{feature.description}</p>
            </div>
          ))}
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div className="space-y-6">
            <h3 className="text-3xl font-bold text-gray-900">
              Our Story & Mission
            </h3>
            <div className="space-y-4 text-gray-600 leading-relaxed">
              <p>
                ADE-HI Integrated Farm Limited was founded with a simple mission: to provide 
                high-quality, healthy livestock to customers who value excellence. We specialize 
                in pig farming and have built our reputation on trust, quality, and exceptional service.
              </p>
              <p>
                Our farm employs modern farming techniques combined with traditional care methods 
                to ensure our animals are healthy, happy, and ready for their new homes. We maintain 
                detailed records of each animal's health, weight, and development.
              </p>
              <p>
                Whether you're a commercial buyer, restaurant owner, or individual customer, 
                we provide personalized service and support to meet your specific needs.
              </p>
            </div>
            <div className="flex items-center space-x-8">
              <div>
                <div className="text-3xl font-bold text-primary-600">1000+</div>
                <div className="text-sm text-gray-500">Animals Sold</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-primary-600">98%</div>
                <div className="text-sm text-gray-500">Customer Satisfaction</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-primary-600">24/7</div>
                <div className="text-sm text-gray-500">Support Available</div>
              </div>
            </div>
          </div>
          <div className="relative">
            <img
              src="https://images.pexels.com/photos/1599459/pexels-photo-1599459.jpeg?auto=compress&cs=tinysrgb&w=800"
              alt="ADE-HI Farm facilities"
              className="rounded-2xl shadow-lg w-full"
            />
          </div>
        </div>
      </div>
    </section>
  )
}

export default About