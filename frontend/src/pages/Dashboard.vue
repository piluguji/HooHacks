<template>
  <div class="content">
  <br/>
    <div style="width:100vw">
      <div id="AAPL">
        <span> AAPL </span>
      </div>
      <div id="name">
      Showing Risk Analysis for: Apple Inc
      </div>
    </div>
    <br/>
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-95"
        style="margin-left:10px;"
      >
        <chart-card
          :chart-data="dailySalesChart.data"
          :chart-options="dailySalesChart.options"
          :chart-type="'Line'"
          data-background-color="green"
        >
          <template slot="content">
            <h4 id="title">Predicted PDF in 1 Month</h4>
            <br/>
            <span class="bt" v-on:click="oneweek">1 Week View</span>
             <span class="bt">1 Month View</span>
              <span class="bt">1 Year View</span>
          </template>
        </chart-card>
      </div>

      <div
        class="x md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-30"
        style="margin-left: 10px;"
      >
        <stats-card data-background-color="green">
          <template slot="header">
            <md-icon>info_outline</md-icon>
          </template>

          <template slot="content"><br/>
            <b><p class="category" style="text-color:blue;font-size:40px;">Risk Index</p></b><br/>
            <h3 class="title">{{this.riskNumber}} / 100</h3>
          </template>

        </stats-card>
      </div>


      <div
        class="x md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-30"
        style="margin-left: 50px;"
      >
        <stats-card data-background-color="orange">
          <template slot="header">
            <md-icon>store</md-icon>
          </template>

           <template slot="content"><br/>
            <b><p class="category" style="text-color:blue;font-size:40px;">Confidence Index</p></b><br/>
            <h3 class="title">{{this.confidenceNumber}}%</h3>
          </template>

        </stats-card>
      </div>

      <div
        class="x md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-30"
        style="margin-left: 50px;"
      >
        <stats-card data-background-color="green">
          <template slot="header">
            <md-icon>content_copy</md-icon>
          </template>

           <template slot="content"><br/>
            <b><p class="category" style="text-color:blue;font-size:40px;">Volatility Index</p></b><br/>
            <h3 class="title">{{this.volNumber}} / 100</h3>
          </template>

        </stats-card>
      </div>

    </div>
  </div>
</template>

<script>
import Chart from 'chart.js'

import {
  StatsCard,
  ChartCard,
  NavTabsCard,
  NavTabsTable,
} from "@/components";

export default {
  mounted() {

  },
  components: {
    StatsCard,
    ChartCard,
  },
  data() {
    return {
      riskNumber: 12,
      confidenceNumber: 78,
      volNumber: 13,
      dailySalesChart: {
        data: {
          labels: ['169.0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '170.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '172.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '174.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '177.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '178.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '180.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '182.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '184.9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          series: [[0.01479108, 0.0150234 , 0.01537551, 0.01585483, 0.01634929,
       0.01685953, 0.0173862 , 0.01792997, 0.01849154, 0.01907162,
       0.01967093, 0.02029023, 0.02093027, 0.02159185, 0.02227575,
       0.02298281, 0.02371385, 0.02446971, 0.02525127, 0.02606311,
       0.02692554, 0.02785749, 0.02884917, 0.02988507, 0.03096293,
       0.03208397, 0.03324939, 0.03446037, 0.03571804, 0.03702411,
       0.03838289, 0.03979831, 0.04126936, 0.04279404, 0.04437249,
       0.04600535, 0.0476931 , 0.04943612, 0.05123458, 0.05308852,
       0.05499786, 0.05696228, 0.05898109, 0.06105328, 0.06317769,
       0.06535282, 0.0675769 , 0.0698478 , 0.07216302, 0.07451848,
       0.0769046 , 0.07931218, 0.08174137, 0.08419354, 0.08666499,
       0.0891504 , 0.09164403, 0.09413966, 0.09663065, 0.09910767,
       0.10155165, 0.10394499, 0.10628783, 0.10858284, 0.11082372,
       0.11300167, 0.11510772, 0.11713278, 0.11906763, 0.12090074,
       0.12261125, 0.12418067, 0.12560947, 0.12690097, 0.12804968,
       0.12904823, 0.12988976, 0.13056797, 0.13107723, 0.13140959,
       0.13154599, 0.13147173, 0.13119748, 0.13073768, 0.1300954 ,
       0.12927165, 0.12826838, 0.12708853, 0.12573594, 0.12421326,
       0.12251568, 0.12064217, 0.11861015, 0.11643935, 0.114141  ,
       0.11172468, 0.1092004 , 0.10657858, 0.10386992, 0.10108291,
       0.09821686, 0.09527487, 0.09227998, 0.08925631, 0.08621703,
       0.0831724 , 0.08013227, 0.077106  , 0.07410245, 0.07112817,
       0.06818268, 0.06526772, 0.06239856, 0.0595904 , 0.05684999,
       0.0541816 , 0.05158886, 0.04907474, 0.04664166, 0.04428998,
       0.04201412, 0.03981051, 0.03768698, 0.03565128, 0.03370412,
       0.03184429, 0.0300703 , 0.02838038, 0.02677251, 0.02524348,
       0.02378612, 0.02239489, 0.02107244, 0.0198216 , 0.01864045,
       0.01752598, 0.01647521, 0.01548516, 0.01455291, 0.01367508,
       0.01284643, 0.01206265, 0.01132372, 0.01062982, 0.00997891,
       0.0093685 , 0.00879621, 0.00825975, 0.00775696, 0.00728547,
       0.00684177, 0.00642298, 0.00602897, 0.00565982, 0.00531423,
       0.00499066, 0.00468769, 0.00440394, 0.00413816, 0.00388908,
       0.00365522, 0.0034353 , 0.00322871, 0.00303494, 0.00285321,
       0.00268271, 0.0025227 , 0.00237248, 0.00223139, 0.00209884,
       0.00197426, 0.00185712, 0.00174694, 0.00164327, 0.00154568,
       0.00145379, 0.00136722, 0.00128565, 0.00122686, 0.00118845]],
        },
        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0,
          }),
          low: 0,
          high: 0.17, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0,
          },
        },
      },
      
    };
  },
  methods: {
    oneweek() {
      this.riskNumber += 7;
      

    }
  },
};
</script>

<style>
#AAPL {
  font-size: 50px;
  background-color: white;
  border-radius: 5px;
  border-color: black;
  height: 10vh;
  width: 20vw;
  padding-left: 30px;
  padding-top: 35px;
  border: 3px solid #888888; 
  display: inline-block;  
}
#name {
  display: inline-block; 
  margin-left: 30px;
  font-size: 50px;
  width: 70vw;
  text-align: right;
  color: black;
}
.xi {
  width: 40em;
}
#title {
  font-size:50px;
}

.title {
  font-size: 38px;
}

.bt {
  color: blue;
  font-size: 35px;
  margin-left: 28px;
}

html {
  overflow-x:hidden;
}
.x !important {
  height:300vh;
}

.ct-chart {
  height:40vh;
}
</style>
