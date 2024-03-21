import React, { useState } from "react";
import axios from "axios";
import Button from "@mui/material/Button";
import SendIcon from "@mui/icons-material/Send";
import { TextField } from "@mui/material";
import Grid from "@mui/material/Grid"; // Grid version 1
import Card from "@mui/material/Card";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import CardContent from "@mui/material/CardContent";
import { Chip, Stack } from "@mui/material";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import { useEffect } from "react";
import { useRef } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFileExcel } from "@fortawesome/free-solid-svg-icons";


const RasaChatWidget = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");
  const [showButtons, setShowButtons] = useState(false); // State to control button visibility
  const textFieldRef = useRef(null);

  useEffect(() => {
    textFieldRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleUserInput = (event) => {
    setUserInput(event.target.value);
  };

  const addMessage = (text, sender) => {
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: ` ${text}`, sender },
    ]);
  };

  const sendMessage = async () => {
    setUserInput("");
    try {
      addMessage(`${userInput}`, "You");
      const response = await axios.post(
        "http://localhost:5005/webhooks/rest/webhook",
        {
          sender: "test_user",
          message: userInput,
        }
      );

      const botResponses = response.data.map((botMsg) => ({
        text: botMsg.text,
        sender: "Bot",
      }));

      botResponses.forEach((botMsg) => {
        addMessage(botMsg.text, "Bot");
        if (botMsg.text === "Hey! How are you?") {
          setShowButtons(true); // Show buttons when the bot message is "Hey! How are you?"
        }
      });
    } catch (error) {
      console.error("Error sending message to Rasa:", error);
    }
  };

  const handleButtonClick = (payload) => {
    setShowButtons(false); // Hide buttons when a button is clicked
    addMessage(payload, "You");
    sendMessageToRasa(payload);
  };

  const sendMessageToRasa = async (payload) => {
    try {
      const response = await axios.post(
        "http://localhost:5005/webhooks/rest/webhook",
        {
          sender: "test_user",
          message: payload,
        }
      );

      const botResponses = response.data.map((botMsg) => ({
        text: botMsg.text,
        sender: "Bot",
      }));

      botResponses.forEach((botMsg) => {
        addMessage(botMsg.text, "Bot");
      });
    } catch (error) {
      console.error("Error sending message to Rasa:", error);
    }
  };

  return (
    <div>
      <Grid container spacing={4}>
        <Grid item xs={6}>
          <Card
            variant="outlined"
            style={{ margin: "30px", marginRight: "0px" }}
          >
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                Query Type 1 (without Software Name)
              </Typography>

              <Divider dark />
              <Typography
                color="text.secondary"
                variant="body1"
                style={{ width: "100%", padding: "4%" }}
              >
                Tell me the Architect
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={6}>
          <Card
            variant="outlined"
            style={{ margin: "30px", marginLeft: "0px" }}
          >
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                Query Type 2 (with Software Name)
              </Typography>

              <Divider dark />

              <Typography
                color="text.secondary"
                variant="body1"
                style={{ width: "100%", padding: "4%" }}
              >
                Who is the Architect of Skype?
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid container alignItems="center" justify="center">
          <Grid item style={{ margin: "auto" }}>
            <Button
              style={{ padding: "15px", width: "200px" }}
              variant="contained"
              color="success"
              onClick={() => {
                const url =
                  "https://docs.google.com/spreadsheets/d/1HOWNA73XOXH_59mGouW0UJhP-wp5VzdG/edit?usp=sharing&ouid=112216604259922803315&rtpof=true&sd=true";
                window.open(url, "_blank");
              }}
              endIcon={<FontAwesomeIcon icon={faFileExcel} />}
            >
              Excel Data
            </Button>
          </Grid>
        </Grid>

        <Grid item xs={12}>
          <Stack
            direction="row"
            spacing={1}
            style={{ width: "auto", padding: "2%" }}
          >
            <Chip
              label="Architect"
              color="primary"
              style={{ width: "100%", fontSize: "1em" }}
            />
            <Chip
              label="Vendor"
              color="primary"
              style={{ width: "100%", fontSize: "1em" }}
            />
            <Chip
              label="Phaseout Date"
              color="primary"
              style={{ width: "100%", fontSize: "1em" }}
            />
            <Chip
              label="Installation Count"
              color="primary"
              style={{ width: "100%", fontSize: "1em" }}
            />
            <Chip
              label="License Required"
              color="primary"
              style={{ width: "100%", fontSize: "1em" }}
            />
            <Chip
              label="TSC Status"
              color="primary"
              style={{ width: "100%", fontSize: "1em" }}
            />
          </Stack>
        </Grid>
      </Grid>

      <List style={{ paddingLeft: "%" }}>
        {messages.map((msg, index) => (
          <ListItem key={index}>
            <ListItemText
              primary={
                <span>
                  <strong>{msg.sender}: </strong>
                  {msg.text}
                </span>
              }
            />
          </ListItem>
        ))}
      </List>

       {/* Display buttons if showButtons is true */}
      
      {showButtons && (
         <Grid container alignItems="center" justify="center" spacing={2} style={{marginTop: '20px'}}>
         <Grid item xs={12} style={{ padding: "2%" }}>
           <Typography variant="h6" gutterBottom style={{ textAlign: "center" }}>
             What are you looking for? (Pick any)
           </Typography>
           <div style={{ display: "flex", justifyContent: "center" , gap: '15px'}}>
             <Button variant="contained" onClick={() => handleButtonClick("/get_architect")}>
               Find Architect
             </Button>
             <Button variant="contained" onClick={() => handleButtonClick("/get_vendor_name")}>
               Find Vendor
             </Button>
             <Button variant="contained" onClick={() => handleButtonClick("/check_license_required")}>
               License Status
             </Button>
             <Button variant="contained" onClick={() => handleButtonClick("/check_tsc_status")}>
               TSC Status
             </Button>
             <Button variant="contained" onClick={() => handleButtonClick("/get_installation_count")}>
               Installation Count
             </Button>
             <Button variant="contained" onClick={() => handleButtonClick("/get_phaseout_date")}>
               Phaseout Date
             </Button>
           </div>
         </Grid>
       </Grid>
     )}

      <Grid container alignItems="center" justify="center" spacing={2}>
        <Grid item xs={10} style={{ padding: "2%" }}>
          <TextField
            inputRef={textFieldRef}
            id="outlined-basic"
            variant="outlined"
            type="text"
            value={userInput}
            onChange={handleUserInput}
            onKeyPress={(event) => {
              if (event.key === "Enter") {
                sendMessage();
              }
            }}
            placeholder="Type a message..."
            style={{ width: "97%", padding: "4%" }}
          />
        </Grid>

        <Grid item xs={2} style={{ padding: "0%" }}>
          <Button
            style={{ padding: "15px" }}
            variant="contained"
            endIcon={<SendIcon />}
            onClick={sendMessage}
          >
            Send
          </Button>
        </Grid>
      </Grid>

     
   </div>
 );
};

export default RasaChatWidget;