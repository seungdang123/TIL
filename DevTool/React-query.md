import { useState, useEffect } from "react";
import { useQuery } from "react-query";
import axios from "axios";

function App() {
// # axios를 이용한 일반적인 서버 통신

// const [isLoading, setLoading] = useState(false);
// const [isError, setError] = useState(false);
// const [data, setData] = useState({});

// const fetchData = async () => {
// setError(false);
// setLoading(true);

// try {
// const response = await axios("https://random.dog/woof.json");

// setData(response.data);
// } catch (error) {
// setError(true);
// }

// setLoading(false);
// };

// useEffect(() => {
// fetchData();
// }, []);

// # react-query & axios를 이용한 서버 통신
// # 상태 관리를 보다 쉽고 간결하게 할 수 있다

const { isLoading, error, data } = useQuery("dogs", () =>
axios("https://random.dog/woof.json")
);

if (error) return <h1>Error: {error.message}, try again!</h1>;
if (isLoading) return <h1>Loading...</h1>;

return (
<div
className="App"
style={{
        height: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }} >
<img
src={data.data.url}
alt="dog.jpg"
style={{ width: "800px", height: "800px" }}
/>
</div>
);
}

export default App;
