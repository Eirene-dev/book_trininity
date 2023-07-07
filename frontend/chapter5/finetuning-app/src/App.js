import React from 'react';
import {
  ChakraProvider,
  Box,
  Text,
  VStack,
  Grid,
  theme,
  Avatar,
  Flex
} from '@chakra-ui/react';
import { ColorModeSwitcher } from './ColorModeSwitcher';
import { Heading } from '@chakra-ui/react'
import MenuBar from "./MenuBar";
import Chat from "./Chat";
import FineTuning from './FineTuning';
import Settings from './Settings';

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function HomePage() {
  return (
    <Box textAlign="center" fontSize="xl">
      <Grid minH="100vh" p={2}>
      <VStack spacing={2}>
        <Heading>Fine-tuning Chat</Heading>
        <Text>
          You can use ChatGPT with fine-tuned models.
          </Text>
        </VStack>
      </Grid>
    </Box>
  );
}

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Router>
        <Flex justifyContent="space-between" alignItems="center" mb={4}>
          <Flex alignItems="center">
            <MenuBar />
            <Text ml={2}>Fine Chat</Text>
          </Flex>
          <Flex alignItems="center">
            <Avatar size='sm' name='Kent Dodds' src='https://bit.ly/kent-c-dodds' />
            <ColorModeSwitcher justifySelf="flex-end" ml={2} />
          </Flex>
        </Flex>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/finetuning" element={<FineTuning />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
