import { Calendar, Copyright as Weight, MapPin, Phone } from 'lucide-react'
import AnimalCard from './AnimalCard'

const Animals = () => {
  const animals = [
    {
      id: 1,
      name: 'Premium Boar - Chester',
      breed: 'Large White Yorkshire',
      age: '18 months',
      weight: '180 kg',
      price: '₦85,000',
      image: 'https://images.pexels.com/photos/1300355/pexels-photo-1300355.jpeg?auto=compress&cs=tinysrgb&w=500',
      description: 'Excellent breeding boar with proven genetics and strong build.',
      status: 'Available',
      healthStatus: 'Excellent',
      vaccinated: true
    },
    {
      id: 2,
      name: 'Breeding Sow - Bella',
      breed: 'Hampshire',
      age: '2 years',
      weight: '160 kg',
      price: '₦75,000',
      image: 'https://images.pexels.com/photos/1300359/pexels-photo-1300359.jpeg?auto=compress&cs=tinysrgb&w=500',
      description: 'Proven breeder with excellent maternal instincts and health record.',
      status: 'Available',
      healthStatus: 'Excellent',
      vaccinated: true
    },
    {
      id: 3,
      name: 'Market Ready - Max',
      breed: 'Duroc Cross',
      age: '8 months',
      weight: '95 kg',
      price: '₦42,000',
      image: 'https://images.pexels.com/photos/1300354/pexels-photo-1300354.jpeg?auto=compress&cs=tinysrgb&w=500',
      description: 'Ready for market with excellent meat quality and marbling.',
      status: 'Available',
      healthStatus: 'Excellent',
      vaccinated: true
    },
    {
      id: 4,
      name: 'Young Gilt - Luna',
      breed: 'Landrace',
      age: '6 months',
      weight: '65 kg',
      price: '₦35,000',
      image: 'https://images.pexels.com/photos/1300358/pexels-photo-1300358.jpeg?auto=compress&cs=tinysrgb&w=500',
      description: 'Young female pig perfect for breeding program development.',
      status: 'Available',
      healthStatus: 'Excellent',
      vaccinated: true
    },
    {
      id: 5,
      name: 'Premium Piglets Set',
      breed: 'Mixed Heritage',
      age: '8 weeks',
      weight: '12-15 kg each',
      price: '₦15,000 each',
      image: 'https://images.pexels.com/photos/1300356/pexels-photo-1300356.jpeg?auto=compress&cs=tinysrgb&w=500',
      description: 'Healthy piglets from champion bloodlines, sold in sets of 4+.',
      status: 'Available',
      healthStatus: 'Excellent',
      vaccinated: true
    },
    {
      id: 6,
      name: 'Heavy Boar - Thunder',
      breed: 'Large Black',
      age: '3 years',
      weight: '220 kg',
      price: '₦95,000',
      image: 'https://images.pexels.com/photos/1300360/pexels-photo-1300360.jpeg?auto=compress&cs=tinysrgb&w=500',
      description: 'Champion bloodline boar with exceptional size and genetics.',
      status: 'Reserved',
      healthStatus: 'Excellent',
      vaccinated: true
    }
  ]

  return (
    <section id="animals" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto section-padding">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Our Premium Livestock
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Browse our current selection of healthy, well-cared-for pigs. Each animal comes with 
            complete health records, vaccination history, and quality guarantee.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {animals.map((animal) => (
            <AnimalCard key={animal.id} animal={animal} />
          ))}
        </div>

        <div className="mt-16 text-center">
          <div className="bg-white rounded-2xl p-8 shadow-lg max-w-2xl mx-auto">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              Looking for Something Specific?
            </h3>
            <p className="text-gray-600 mb-6 leading-relaxed">
              We regularly receive new animals and can help you find exactly what you're looking for. 
              Contact us with your specific requirements.
            </p>
            <a href="#contact" className="btn-primary">
              Contact Us for Custom Orders
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Animals