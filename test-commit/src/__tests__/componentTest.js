import React from 'react';
import { render } from '@testing-library/react';
import MyComponent from '../component';

describe('MyComponent', () => {
 it('renders correctly', () => {
   const { getByText } = render(<MyComponent />);
   expect(getByText('Hell World!')).toBeInTheDocument();
 });
});