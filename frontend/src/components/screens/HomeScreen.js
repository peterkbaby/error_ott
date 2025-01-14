import React, { useEffect } from 'react';
import { Row, Col } from 'react-bootstrap';
import { useDispatch, useSelector } from 'react-redux';
import { listVideos } from '../../actions/videoActions';
import Video from '../Video';

function HomeScreen() {
  const dispatch = useDispatch();
  const videoList = useSelector(state => state.videoList);
  const { error, loading, videos } = videoList;

  useEffect(() => {
    dispatch(listVideos());
  }, [dispatch]);

  return (
    <div>
      <h1>Recent Movies</h1>
      {loading ? (
        <h2>Loading...</h2>
      ) : error ? (
        <h3>{error}</h3>
      ) : (
        <Row>
          {videos.map(video => (
            <Col key={video.id} sm={12} md={6} lg={4} xl={3}>
              <Video video={video} />
            </Col>
          ))}
        </Row>
      )}
    </div>
  );
}

export default HomeScreen;
