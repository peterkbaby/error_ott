// src/components/Video.js
import React from 'react';
import { Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function Video({ video }) {
  return (
    <Card className='my-3 p-3 rounded' style={{ width: '300px', height: '300px' }}>
      <Link to={`/video/${video.id}`}>
        <Card.Img src={video.thumbnail} style={{ width: '100%', height: '200px' }} />
      </Link>
      <Card.Body>
        <Link to={`/video/${video.id}`}>
          <Card.Title>
            <strong>{video.title}</strong>
          </Card.Title>
        </Link>
        <Card.Text as='h3'>
          {video.category}
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Video;
