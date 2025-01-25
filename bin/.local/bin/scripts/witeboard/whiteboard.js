#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');

// Get the file extension from the arguments
const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Usage: create-file <extension>');
  process.exit(1);
}

const extension = args[0];

// Generate a random filename with the provided extension
const fileName = `file_${Date.now()}.${extension}`;
const filePath = path.join('/tmp', fileName);

try {
  // Open the file in nvim
  execSync(`nvim ${filePath}`, { stdio: 'inherit' });
} catch (error) {
  console.error('Error creating file:', error.message);
  process.exit(1);
}

