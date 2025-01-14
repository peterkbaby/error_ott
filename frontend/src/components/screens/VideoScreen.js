import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import { listVideoDetails } from '../../actions/videoActions';
import { Container, Row, Col } from 'react-bootstrap';

function VideoScreen() {
  const { id } = useParams();
  const dispatch = useDispatch();

  const videoDetails = useSelector((state) => state.videoDetails);
  const { loading, error, video } = videoDetails;

  useEffect(() => {
    dispatch(listVideoDetails(id));
  }, [dispatch, id]);

  return (
    <Container>
      {loading ? (
        <h2>Loading...</h2>
      ) : error ? (
        <h3>{error}</h3>
      ) : (
        video && (
          <Row>
            <Col md={8}>
              <video width="100%" controls>
                <source src={`${process.env.REACT_APP_API_URL}${video.videoFile}`} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
            </Col>
            <Col md={4}>
              <h1>{video.title}</h1>
              <p>{video.description}</p>
              <p>Category: {video.category}</p>
            </Col>
          </Row>
        )
      )}
    </Container>
  );
}

export default VideoScreen;
