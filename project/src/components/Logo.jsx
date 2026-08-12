import React from 'react';

const Logo = ({ size = 'md', variant = 'light' }) => {
  const sizeClasses = {
    sm: { img: 'w-8 h-8', title: 'text-lg', subtitle: 'text-xs' },
    md: { img: 'w-11 h-11', title: 'text-xl', subtitle: 'text-xs' },
    lg: { img: 'w-16 h-16', title: 'text-2xl', subtitle: 'text-sm' },
  }[size] || { img: 'w-11 h-11', title: 'text-xl', subtitle: 'text-xs' };

  const isDark = variant === 'dark';

  return (
    <a href="#home" className="flex items-center space-x-3 group transition-transform duration-200 hover:scale-[1.02]">
      <div className={`${sizeClasses.img} rounded-xl overflow-hidden shadow-md group-hover:shadow-lg transition-all duration-300 ring-2 ring-emerald-500/20 flex-shrink-0 bg-white p-0.5`}>
        <img 
          src="/logo.jpg" 
          alt="ADE-HI Integrated Farm Logo" 
          className="w-full h-full object-cover rounded-lg"
          onError={(e) => {
            // Fallback SVG if image fails to load
            e.target.style.display = 'none';
            e.target.nextSibling.style.display = 'flex';
          }}
        />
        <div className="hidden w-full h-full bg-emerald-700 text-white font-bold flex items-center justify-center rounded-lg text-sm">
          AH
        </div>
      </div>
      <div className="flex flex-col">
        <span className={`font-extrabold tracking-tight ${sizeClasses.title} ${isDark ? 'text-white' : 'text-gray-900'} group-hover:text-emerald-600 transition-colors`}>
          ADE-HI
        </span>
        <span className={`font-semibold tracking-wider uppercase ${sizeClasses.subtitle} ${isDark ? 'text-emerald-200/90' : 'text-emerald-700'}`}>
          Integrated Farm Ltd
        </span>
      </div>
    </a>
  );
};

export default Logo;
