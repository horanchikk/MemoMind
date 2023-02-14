tailwind.config = {
  theme: {
    extend: {
      colors: {
            'back': '#080f11',
            'fore': '#c44b79',
            'code-back': '#acacac',
            'back-light': '#f2cedb',
            'fore-light': '#ee4968',
          }
    },
    screens: {
      'mobile': {'max': '640px'},
      'tablet': {'min': '641px', 'max': '1280px'},
      'desktop': {'min': '1281px'}
    }
  }
}