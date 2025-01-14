import React from 'react'

import { Pagination } from 'react-bootstrap'

export default function paginate() {
  return (
    <Pagination>
    {[...Array(pages).keys()].map((x) => (
        <LinkContainer
            key={x + 1}
           
        >
            <Pagination.Item active={x + 1 === page}>{x + 1}</Pagination.Item>
        </LinkContainer>
    ))}
</Pagination>
  )
}


