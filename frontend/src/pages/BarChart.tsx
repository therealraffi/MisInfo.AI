import { Bar } from "react-chartjs-2";
// import annotationPlugin from "chartjs-plugin-annotation";

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend,
    BarElement
  } from 'chart.js';

const BarChart = ({data, questions, axis}: {data: any, questions: any, axis: string}) => {

    ChartJS.register(
        CategoryScale,
        LinearScale,
        PointElement,
        BarElement,
        Title,
        Tooltip,
        Legend,
    );

    const labels: any[] = [];
    const values: any[] = [];
    const colors = ['#1DC690', '#278AB0', '#1C4670', '#EAEAE0'];

    for (const entry of data) {
        labels.push(entry['category']);
        values.push(entry['score']);
    }

    let created_data = {
        labels: labels,
        datasets: [{
            data: values,
            label: 'score',
            borderWidth: 1,
            backgroundColor: colors
        }]
    };
      

    return (
        <div className={"relative block max-w-3xl p-6 bg-white border border-gray-200 rounded-lg shadow-lg"}>
            <Bar data={created_data} options={
                {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false,
                        },
                        title: {
                            display: false,
                        },
                    },
                    scales: {
                        y: {
                            title: {
                                display: true,
                                text: 'Score'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: axis
                            }
                        },
                    }
                }
            } />
        </div>
    )

}

export default BarChart;