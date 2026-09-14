function WeakTopics({ topics }) {
  return (
    <div>
      <h2>Weak Topics</h2>

      <ul>
        {topics.map((topic, index) => (
          <li key={index}>{topic}</li>
        ))}
      </ul>
    </div>
  );
}

export default WeakTopics;