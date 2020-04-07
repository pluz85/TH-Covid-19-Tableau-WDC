(function () {
    const myConnector = tableau.makeConnector();

    myConnector.init = function(initCallback) {

			if (tableau.phase === tableau.phaseEnum.interactivePhase || tableau.phase === tableau.phaseEnum.authPhase) {
				console.log("Tableau Detected");
				$("#noTableau").addClass('d-none');
                $("#Tableau").removeClass('d-none');
                $("#submitButton").click(function () {
                tableau.connectionName = "Covid-19 TH Daily";
                tableau.submit();
        });
			}
			initCallback();
		};

    myConnector.getSchema = function (schemaCallback) {

        const daily_cols = [
            {id: "Confirmed", alias: "ติดเชื้อสะสม", dataType: tableau.dataTypeEnum.int},
            {id: "Recovered", alias: "หายแล้ว", dataType: tableau.dataTypeEnum.int},
            {id: "Hospitalized", alias: "รักษาในโรงพยาบาล", dataType: tableau.dataTypeEnum.int},
            {id: "Deaths", alias: "เสียชีวิต", dataType: tableau.dataTypeEnum.int},
            {id: "NewConfirmed", alias: "ติดเชื่อเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "NewRecovered", alias: "รักษาหายเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "NewHospitalized", alias: "รักษาในโรงพยาบาลเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "NewDeaths", alias: "เสียชีวิตเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "UpdateDate", alias: "อัพเดตข้อมูลล่าสุด", dataType: tableau.dataTypeEnum.datetime}
        ];
        const todayTable = {
            id: "TH_COVID_TODAY",
            alias: "สรุปข้อมูล Covid-19 ประจำวัน",
            columns: daily_cols
        };

        const timeline_cols = [
            {id: "Date", alias: "วันที่", dataType: tableau.dataTypeEnum.datetime},
            {id: "Confirmed", alias: "ติดเชื้อสะสม", dataType: tableau.dataTypeEnum.int},
            {id: "Recovered", alias: "หายแล้ว", dataType: tableau.dataTypeEnum.int},
            {id: "Hospitalized", alias: "รักษาในโรงพยาบาล", dataType: tableau.dataTypeEnum.int},
            {id: "Deaths", alias: "เสียชีวิต", dataType: tableau.dataTypeEnum.int},
            {id: "NewConfirmed", alias: "ติดเชื่อเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "NewRecovered", alias: "รักษาหายเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "NewHospitalized", alias: "รักษาในโรงพยาบาลเพิ่ม", dataType: tableau.dataTypeEnum.int},
            {id: "NewDeaths", alias: "เสียชีวิตเพิ่ม", dataType: tableau.dataTypeEnum.int}
        ];

        const timelineTable = {
            id: "TH_COVID_TIMELINE",
            alias: "ข้อมูลสรุปตามช่วงเวลา",
            columns: timeline_cols
        };

        const case_cols = [
            {id: "ConfirmDate", alias: "วันที่", dataType: tableau.dataTypeEnum.datetime},
            {id: "No", alias: "เคส", dataType: tableau.dataTypeEnum.string},
            {id: "Age", alias: "อายุ", dataType: tableau.dataTypeEnum.int},
            {id: "Gender", alias: "เพศ", dataType: tableau.dataTypeEnum.string},
            {id: "GenderEn", alias: "Gender", dataType: tableau.dataTypeEnum.string},
            {id: "Nation", alias: "สัญชาติ", dataType: tableau.dataTypeEnum.string},
            {id: "NationEn", alias: "Nationality", dataType: tableau.dataTypeEnum.string},
            {
                id: "Province",
                alias: "จังหวัด",
                geoRole: tableau.geographicRoleEnum.state_province,
                dataType: tableau.dataTypeEnum.string
            },
            {
                id: "ProvinceID",
                alias: "รหัสจังหวัด",
                description: "สามารถนำไปทำ relation กับ Province ID แผนที่ GeoJson ได้",
                dataType: tableau.dataTypeEnum.string
            },
            {
                id: "ProvinceEn",
                alias: "Province",
                geoRole: tableau.geographicRoleEnum.state_province,
                dataType: tableau.dataTypeEnum.string
            }
        ];
        const caseTable = {
            id: "TH_COVID_CASE",
            alias: "ข้อมูลแต่ละเคส",
            columns: case_cols
        };

        const risk_cols = [
            {id: "Date", alias: "วันที่", dataType: tableau.dataTypeEnum.string},
            {id: "Time", alias: "ห้วงเวลา", dataType: tableau.dataTypeEnum.string},
            {id: "Detail", alias: "รายละเอียด", dataType: tableau.dataTypeEnum.string},
            {id: "Location", alias: "สถานที่", dataType: tableau.dataTypeEnum.string},
            {id: "Recommend", alias: "คำแนะนำ", dataType: tableau.dataTypeEnum.string},
            {id: "AnnounceBy", alias: "ผู้ประกาศ", dataType: tableau.dataTypeEnum.string},
            {
                id: "Province",
                alias: "จังหวัด",
                geoRole: tableau.geographicRoleEnum.state_province,
                dataType: tableau.dataTypeEnum.string
            },
            {
                id: "ProvinceEn",
                alias: "Province",
                geoRole: tableau.geographicRoleEnum.state_province,
                dataType: tableau.dataTypeEnum.string
            },
            {id: "Update", alias: "ปรับปรุงข้อมูลล่าสุด", dataType: tableau.dataTypeEnum.datetime}
        ];
        const riskTable = {
            id: "TH_COVID_RISK",
            alias: "แจ้งเตือนพื้นที่ตามคำประกาศ",
            columns: risk_cols
        };
        schemaCallback([todayTable, caseTable, riskTable, timelineTable]);
    };

    // Download the data
    myConnector.getData = function(table, doneCallback) {
        if (table.tableInfo.id === 'TH_COVID_TODAY') {
            $.getJSON('/today', function(resp) {
                table.appendRows([resp]);
                doneCallback();
            });
        }

        if (table.tableInfo.id === 'TH_COVID_CASE') {
            $.getJSON('/cases', function(resp) {
                 table.appendRows(resp);
                doneCallback();
            });
        }

        if (table.tableInfo.id === 'TH_COVID_RISK') {
            $.getJSON('/area', function(resp) {
                 table.appendRows(resp);
                doneCallback();
            });
        }
        if (table.tableInfo.id === 'TH_COVID_TIMELINE') {
            $.getJSON('/timeline', function(resp) {
                 table.appendRows(resp);
                doneCallback();
            });
        }
    };

    tableau.registerConnector(myConnector);

    $(document).ready(function () {
        console.log("WDC Ready");

    });
})();