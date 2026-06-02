"""
Frontend README - Installation and Setup
"""

# SecureML Cloud Frontend

A modern, responsive web dashboard for managing encrypted machine learning models built with Next.js, React, and Tailwind CSS.

## Features

- 🎨 Beautiful responsive UI with Tailwind CSS
- 🔐 Secure JWT authentication
- 📊 Interactive dashboards with charts
- 📤 Model upload and management
- 🔮 Encrypted inference interface
- 🔑 Encryption key management
- 📱 Mobile-friendly design
- 🎯 Real-time notifications

## Tech Stack

- **Framework**: Next.js 14
- **UI Library**: React 18
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Charts**: Recharts
- **Notifications**: React Hot Toast
- **Icons**: Lucide React

## Installation

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running (http://localhost:8000)

### Setup

```bash
# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Start development server
npm run dev

# Open browser
# http://localhost:3000
```

## Environment Variables

Create `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx          # Root layout
│   │   ├── page.tsx            # Landing page
│   │   ├── login/              # Login page
│   │   ├── register/           # Registration page
│   │   ├── dashboard/          # Main dashboard
│   │   ├── models/             # Models management
│   │   ├── predictions/        # Predictions interface
│   │   └── settings/           # Settings & key management
│   ├── components/
│   │   └── Navbar.tsx          # Navigation component
│   ├── lib/
│   │   ├── api.ts              # API client
│   │   └── store.ts            # Zustand stores
│   └── app/globals.css         # Global styles
├── public/                      # Static assets
├── package.json
├── tailwind.config.ts
├── next.config.js
└── tsconfig.json
```

## Pages

### Landing Page (`/`)
- Hero section with project overview
- Feature highlights
- CTA buttons for login/signup

### Login Page (`/login`)
- Email/password authentication
- Demo credentials display
- Automatic redirect to dashboard

### Registration Page (`/register`)
- User registration form
- Password validation
- Email verification link

### Dashboard (`/dashboard`)
- Statistics cards
- Weekly predictions chart
- Model distribution chart
- Quick action links

### Models (`/models`)
- List all uploaded models
- Upload new models
- Edit model details
- Delete models
- Model status indicators

### Predictions (`/predictions`)
- Make encrypted predictions
- View prediction history
- Monitor execution times
- Download results

### Settings (`/settings`)
- User account information
- CKKS encryption key management
- Key generation and rotation
- Security information
- API configuration

## API Integration

The frontend uses an axios-based API client with automatic token refresh:

```typescript
import apiClient from '@/lib/api';

// Authentication
await apiClient.login(email, password);
await apiClient.register(email, username, password);

// Models
await apiClient.listModels();
await apiClient.uploadModel(formData);
await apiClient.deleteModel(modelId);

// Predictions
await apiClient.makePrediction(modelId, encryptedInput);
await apiClient.getPredictionHistory();

// Keys
await apiClient.generateKeys('CKKS');
await apiClient.getPublicKey();
```

## State Management

Using Zustand for global state:

```typescript
import { useAuthStore, useModelStore, usePredictionStore } from '@/lib/store';

// Auth
const { user, accessToken, logout, setUser } = useAuthStore();

// Models
const { models, addModel, deleteModel } = useModelStore();

// Predictions
const { predictions, addPrediction } = usePredictionStore();
```

## Build for Production

```bash
# Build
npm run build

# Start production server
npm start

# Or deploy to Vercel
vercel deploy
```

## Testing

```bash
# Run tests
npm test

# Watch mode
npm test -- --watch

# Coverage
npm test -- --coverage
```

## Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Set environment variables
vercel env add NEXT_PUBLIC_API_URL
```

### Docker

```bash
# Build image
docker build -t secureml-frontend .

# Run container
docker run -p 3000:3000 secureml-frontend
```

### Manual Deployment

```bash
# Build
npm run build

# Start
npm start
```

## Environment Variables

### Development
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

### Production
```env
NEXT_PUBLIC_API_URL=https://api.yourdomain.com/api/v1
```

## Performance Optimization

- ✅ Code splitting with Next.js
- ✅ Image optimization
- ✅ Static generation where possible
- ✅ CSS minification with Tailwind
- ✅ API request caching
- ✅ Token refresh optimization

## Security

- ✅ JWT token storage in localStorage
- ✅ Automatic token refresh on 401
- ✅ Protected routes with authentication check
- ✅ HTTPS/TLS in production
- ✅ CORS enabled for API

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### API Connection Errors
```bash
# Verify API is running
curl http://localhost:8000/health

# Check CORS settings
curl -H "Origin: http://localhost:3000" http://localhost:8000/health

# Verify API URL in environment
echo $NEXT_PUBLIC_API_URL
```

### Build Errors
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Page Not Loading
```bash
# Check Next.js build
npm run build

# Check development server
npm run dev
```

## Contributing

1. Create feature branch
2. Make changes
3. Test thoroughly
4. Submit pull request

## License

MIT

## Support

- GitHub Issues: https://github.com/gangjinu/Homomorphic-Encryption-Tool-
- Docs: See /docs directory
- API Reference: http://localhost:8000/docs
