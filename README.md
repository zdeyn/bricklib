# `bricklib`

Augment your Python objects with drop-in behaviours and (soon) signals.

## Overview

`bricklib` is a library designed to enhance your Python objects with modular behaviors and (soon) signals.
It allows you to effortlessly attach and manage relationships between objects through well-defined protocols and mixins.

## Features

### Version 0.1.0

This initial release provides the following protocols and mixins:

- `AttachmentSocket` Protocol
- `Attachment` Protocol
- `AttachmentSocketMixin`
- `AttachmentMixin`

### Functionality

#### Protocols

- `AttachmentSocket`:
  - Represents objects capable of attaching other objects.
  - Requires an `attach(attachment: Attachment)` method.
  - Contains a list of attachments.

- `Attachment`:
  - Represents objects that can be attached to other objects.
  - Requires a `_attach_to(socket: AttachmentSocket)` method.
  - Contains a reference to the parent socket.

#### Mixins

- `AttachmentSocketMixin`:
  - Provides the `attach` method.
  - Implements the `AttachmentSocket` protocol.

- `AttachmentMixin`:
  - Provides the `_attach_to` method.
  - Implements the `Attachment` protocol.

### Example Usage

Here's a basic example demonstrating how to use Bricklib:

```python
from bricklib.mixins import AttachmentSocketMixin, AttachmentMixin
from bricklib.types import AttachmentSocket, Attachment

class MySocket(AttachmentSocketMixin):
    """
    Custom socket class inheriting from AttachmentSocketMixin.
    """
    pass

class MyAttachment(AttachmentMixin):
    """
    Custom attachment class inheriting from AttachmentMixin.
    """
    pass

# Create a socket instance
socket = MySocket()

# Ensure the socket instance implements the AttachmentSocket protocol
assert isinstance(socket, AttachmentSocket)
assert socket.attachments == []  # No attachments initially

# Create an attachment instance
attachment = MyAttachment()

# Ensure the attachment instance implements the Attachment protocol
assert isinstance(attachment, Attachment)
assert attachment.parent is None

# Attach the attachment to the socket
socket.attach(attachment)

# Verify that the attachment was successfully added
assert attachment in socket.attachments
assert socket is attachment.parent
```

### Future Plans

- Allow classes to restrict the subtypes of sockets and attachments they'll accept.
- Enhance typing support to ensure compatibility with both runtime checks and static checkers.

## Installation

To install Bricklib, use pip:

```bash
pip install bricklib
```

## Testing (dev)

To test, use pytest:

```bash
pytest -svv
```


