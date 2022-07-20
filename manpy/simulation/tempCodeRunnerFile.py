shouldYield(
            #     operationTypes={"Setup": 1, "Processing": 1}, methods={"isOperated": 0}
            # ):
            #     self.timeWaitForOperatorStarted = self.env.now
            #     yield self.env.process(self.request())
            #     self.timeWaitForOperatorEnded = self.env.now
            #     self.operatorWaitTimeCurrentEntity += (
            #         self.timeWaitForOperatorEnded - self.timeWaitForOperatorStarted
            #     )