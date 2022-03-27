<template>
  <div class="content">
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
            <h4 id="title">1 Week View</h4>
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
        <stats-card data-background-color="red">
          <template slot="header">
            <md-icon>info_outline</md-icon>
          </template>

          <template slot="content"><br/>
            <b><p class="category" style="text-color:blue;font-size:40px;">Risk Index</p></b><br/>
            <h3 class="title">{{this.riskNumber}}</h3>
          </template>

        </stats-card>
      </div>


      <div
        class="x md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-30"
        style="margin-left: 50px;"
      >
        <stats-card data-background-color="red">
          <template slot="header">
            <md-icon>store</md-icon>
          </template>

           <template slot="content"><br/>
            <b><p class="category" style="text-color:blue;font-size:40px;">Confidence Index</p></b><br/>
            <h3 class="title">{{this.confidenceNumber}}</h3>
          </template>

        </stats-card>
      </div>

      <div
        class="x md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-30"
        style="margin-left: 50px;"
      >
        <stats-card data-background-color="red">
          <template slot="header">
            <md-icon>content_copy</md-icon>
          </template>

           <template slot="content"><br/>
            <b><p class="category" style="text-color:blue;font-size:40px;">Volatility Index</p></b><br/>
            <h3 class="title">{{this.volNumber}}</h3>
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
      riskNumber: 6,
      confidenceNumber: 7,
      volNumber: 2,
      dailySalesChart: {
        data: {
          labels: ["M", "T", "W", "T", "F", "S", "S", "M", "T", "W", "T", "F", "S", "S"],
          series: [[12, 17, 7, 17, 23, 18, 38, 12, 17, 7, 17, 23, 18, 38]],
        },
        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0,
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
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
