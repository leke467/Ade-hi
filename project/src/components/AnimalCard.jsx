import { Calendar, Copyright as Weight, Phone, Shield, Heart } from 'lucide-react'

const AnimalCard = ({ animal }) => {
  const {
    name,
    breed,
    age,
    weight,
    price,
    image,
    description,
    status,
    healthStatus,
    vaccinated
  } = animal

  return (
    <div className="card overflow-hidden">
      {/* Image */}
      <div className="relative">
        <img
          src={image}
          alt={name}
          className="w-full h-64 object-cover"
        />
        <div className="absolute top-4 left-4">
          <span className={`px-3 py-1 rounded-full text-sm font-medium ${
            status === 'Available' 
              ? 'bg-secondary-100 text-secondary-800' 
              : 'bg-yellow-100 text-yellow-800'
          }`}>
            {status}
          </span>
        </div>
        <div className="absolute top-4 right-4">
          <div className="bg-white bg-opacity-90 backdrop-blur-sm rounded-lg px-3 py-2">
            <div className="text-lg font-bold text-gray-900">{price}</div>
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="p-6">
        <div className="mb-4">
          <h3 className="text-xl font-bold text-gray-900 mb-1">{name}</h3>
          <p className="text-primary-600 font-medium">{breed}</p>
        </div>

        <p className="text-gray-600 mb-4 leading-relaxed">{description}</p>

        {/* Details Grid */}
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div className="flex items-center space-x-2">
            <Calendar className="w-4 h-4 text-gray-400" />
            <span className="text-sm text-gray-600">{age}</span>
          </div>
          <div className="flex items-center space-x-2">
            <Weight className="w-4 h-4 text-gray-400" />
            <span className="text-sm text-gray-600">{weight}</span>
          </div>
        </div>

        {/* Health Status */}
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center space-x-2">
            <Heart className="w-4 h-4 text-red-500" />
            <span className="text-sm font-medium text-gray-700">Health: {healthStatus}</span>
          </div>
          {vaccinated && (
            <div className="flex items-center space-x-1">
              <Shield className="w-4 h-4 text-secondary-500" />
              <span className="text-sm text-secondary-600 font-medium">Vaccinated</span>
            </div>
          )}
        </div>

        {/* Action Buttons */}
        <div className="flex gap-3">
          <button className="flex-1 btn-primary text-sm">
            Contact for Details
          </button>
          <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200">
            <Phone className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  )
}

export default AnimalCard