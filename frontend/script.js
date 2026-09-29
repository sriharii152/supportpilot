// ============================================
// CONFIGURATION
// ============================================

const API_URL =
    "http://127.0.0.1:8000";


// ============================================
// CUSTOMER
// ============================================

const customerId =
    "rahul";

const customerName =
    "Rahul Sharma";


// ============================================
// DOM ELEMENTS
// ============================================

const messageInput =
    document.getElementById(
        "messageInput"
    );


const chatBox =
    document.getElementById(
        "chatMessages"
    );


const memoryToggle =
    document.getElementById(
        "memoryToggle"
    );


const memoryText =
    document.getElementById(
        "memoryStatus"
    );


const sendButton =
    document.getElementById(
        "sendButton"
    );


// ============================================
// MEMORY TOGGLE
// ============================================

memoryToggle.addEventListener(
    "change",
    function () {

        if (this.checked) {

            memoryText.innerText =
                "ON";

        } else {

            memoryText.innerText =
                "OFF";

        }

    }
);


// ============================================
// ADD MESSAGE
// ============================================

function addMessage(
    message,
    type
) {

    const wrapper =
        document.createElement(
            "div"
        );


    wrapper.className =
        `message ${type}`;


    const label =
        document.createElement(
            "div"
        );


    label.className =
        "message-label";


    label.innerText =
        type === "user"
            ? "You"
            : "SupportPilot";


    const bubble =
        document.createElement(
            "div"
        );


    bubble.className =
        "bubble";


    bubble.innerText =
        message;


    wrapper.appendChild(
        label
    );


    wrapper.appendChild(
        bubble
    );


    chatBox.appendChild(
        wrapper
    );


    chatBox.scrollTop =
        chatBox.scrollHeight;


    return wrapper;
}


// ============================================
// UPDATE MEMORY PANEL
// ============================================

function updateMemories(
    memories
) {

    const memoryList =
        document.getElementById(
            "memoryList"
        );


    memoryList.innerHTML =
        "";


    if (
        !memories ||
        memories.length === 0
    ) {

        memoryList.innerHTML = `
            <div class="memory-item">
                No relevant memory found.
            </div>
        `;

        return;
    }


    memories.forEach(
        memory => {

            const item =
                document.createElement(
                    "div"
                );


            item.className =
                "memory-item";


            item.innerHTML = `
                <span class="check">✓</span>
                ${escapeHtml(memory)}
            `;


            memoryList.appendChild(
                item
            );

        }
    );

}


// ============================================
// SEND MESSAGE
// ============================================

async function sendMessage() {

    const message =
        messageInput.value.trim();


    if (!message) {

        return;

    }


    // Disable button

    sendButton.disabled =
        true;


    // Display user message

    addMessage(
        message,
        "user"
    );


    // Clear input

    messageInput.value =
        "";


    // Show thinking

    const thinking =
        addMessage(
            "Thinking...",
            "assistant"
        );


    try {

        const response =
            await fetch(
                `${API_URL}/chat`,
                {

                    method:
                        "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify({

                            customer_id:
                                customerId,

                            customer_name:
                                customerName,

                            message:
                                message,

                            memory_enabled:
                                memoryToggle.checked

                        })

                }
            );


        if (!response.ok) {

            throw new Error(
                `Server error: ${response.status}`
            );

        }


        const data =
            await response.json();


        // Remove thinking

        thinking.remove();


        // Display response

        addMessage(
            data.answer,
            "assistant"
        );


        // Update memory panel

        updateMemories(
            data.memories
        );


    }

    catch (error) {

        console.error(
            "Request error:",
            error
        );


        thinking.remove();


        addMessage(

            "I couldn't connect to the SupportPilot backend. " +
            "Please make sure the FastAPI server is running.",

            "assistant"

        );

    }


    finally {

        sendButton.disabled =
            false;

        messageInput.focus();

    }

}


// ============================================
// ENTER KEY
// ============================================

messageInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key ===
            "Enter"
        ) {

            sendMessage();

        }

    }
);


// ============================================
// HTML ESCAPE
// ============================================

function escapeHtml(
    text
) {

    const div =
        document.createElement(
            "div"
        );


    div.innerText =
        text;


    return div.innerHTML;
}