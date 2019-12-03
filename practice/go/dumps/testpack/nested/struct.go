package nesty

import "fmt"

type Dictionary map[string]interface{}

type Check struct {
	Bluff string
}

type DoubleC struct {
	Master string
	Check
}


type Tro struct {
	Master string
}

type Metric struct {
	TagName string `json:"tag_name"`
	ID      int    `json:"id"`
}

type Data struct {
	Port      int      `json:"port"`
	Timeout   int      `json:"timeout"`
	SleepTime int      `json:"sleep_time"`
	Metrics   []Metric `json:"metrics"`
}

type NData struct {
	Port      int `json:"port"`
	Timeout   int `json:"timeout"`
	SleepTime int `json:"sleep_time"`
	Metric    `json:"metric"`
}

type PData struct {
	Port      int `json:"port"`
	Timeout   int `json:"timeout"`
	SleepTime int `json:"sleep_time"`
	*Metric   `json:"metric"`
	*DoubleC
	Tro
}

func GetNesty() {
	fmt.Println("Hello, ä¸ç")

	data := []Dictionary{
		{
			"metrics": []Dictionary{
				{"tag_name": "output_current", "id": 3},
				{"tag_name": "input_voltage", "id": 2},
			},
			"port":       161,
			"timeout":    1,
			"sleep_time": 5,
		},
		{
			"metrics": []Dictionary{
				{"tag_name": "destructor", "id": 10},
			},
			"port":       161,
			"timeout":    1,
			"sleep_time": 4,
		},
	}

	for _, dict := range data {
		fmt.Printf("%v\n", dict)
	}

	dataStruct := []Data{
		Data{
			Port:      161,
			Timeout:   1,
			SleepTime: 5,
			Metrics: []Metric{
				Metric{TagName: "output_current", ID: 3},
				Metric{TagName: "input_voltage", ID: 2},
			},
		},
		Data{
			Port:      161,
			Timeout:   1,
			SleepTime: 4,
			Metrics: []Metric{
				Metric{TagName: "destructor", ID: 10},
			},
		},
	}

	for _, dict := range dataStruct {
		// fmap := convertInterface(dict)
		fmt.Printf("%v\n", dict)
	}

	//pkgErrors := map[string]bool{}
	var pkgErrors = map[string]bool{}

	//pkgErrors := map[string]string{"a": "apple", "b": "banana"}
	pkgErrors["a/b/c"] = false
	fmt.Println(pkgErrors["a/b/c"])

	NdataStruct := NData{
		Port:      161,
		Timeout:   1,
		SleepTime: 5,
		Metric:    Metric{TagName: "coda", ID: 1818},
	}
	fmt.Printf("%v\n", NdataStruct.Metric)

	PdataStruct := PData{
		Port:      161,
		Timeout:   1,
		SleepTime: 5,
		Metric:    &Metric{TagName: "TOT", ID: 9191},
		DoubleC:   &DoubleC{Master: "sss", Check: Check{Bluff: "nono"}},
		Tro: Tro{Master: "hahaha"},
	}

	// Nested field access
	fmt.Printf("%v\n", PdataStruct.Metric.TagName)
	// Promoted Field Name
	fmt.Printf("%v\n", PdataStruct.TagName)
	// Similarly, any methods with receivers on Metric struct, will give way to promoted Methods accessible with PdataStruct.methodcall()

	// Double nested promoted field
	fmt.Printf("%v\n", PdataStruct.Bluff)

	//fmt.Printf("%v\n", PdataStruct.Master)
	// testpack/nested/struct.go:133:32: ambiguous selector PdataStruct.Master
	
	//No override possible. So specify exact field as per nested structure
	fmt.Printf("%v\n", PdataStruct.Tro.Master)
}
