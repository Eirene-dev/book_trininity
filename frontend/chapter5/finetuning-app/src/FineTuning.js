import React, { useState } from 'react';
import { 
    Box, 
    Text, 
    VStack,
    Button, 
    Textarea, 
    Select, 
    Checkbox,
    CheckboxGroup,
    Stack
} from '@chakra-ui/react';

const FineTuningScreen = () => {
  const [isFineTuned, setIsFineTuned] = useState(false);
  const [willBeTuned, setWillBeTuned] = useState(false);

  const handleFineTune = () => {
    // Add your fine-tuning logic here
  };

  return (
    <Box p={5}>
      <Text fontSize="2xl">Fine-tuned model</Text>
      <Select placeholder="Select model" my={3}>
        {/* Populate with available models */}
      </Select>
      <Text>Prompt:</Text>
      <Textarea placeholder="Enter the prompt here" my={3} />
      <Text>Completion:</Text>
      <Textarea placeholder="Enter the completion here" my={3} />
      <VStack spacing={2}>
        <CheckboxGroup colorScheme='green' defaultValue={['naruto', 'kakashi']}>
            <Stack spacing={[1, 5]} direction={['column', 'row']}>
                <Checkbox 
                    isChecked={isFineTuned} 
                    onChange={e => setIsFineTuned(e.target.checked)}
                    my={3}
                >
                    Is fine-tuned
                </Checkbox>
                <Checkbox 
                    isChecked={willBeTuned} 
                    onChange={e => setWillBeTuned(e.target.checked)}
                    my={3}
                >
                    Will be tuned
                </Checkbox>
            </Stack>
            </CheckboxGroup>

        <Button onClick={handleFineTune} colorScheme="teal">
            Fine-tuning
        </Button>
      </VStack>
    </Box>
  );
};

export default FineTuningScreen;
