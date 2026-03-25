import numpy as np

def check_close(val, expected, name, rtol=1.0e-3,atol=0.0, feedback_fail="") :
    if abs(val-expected) > atol + rtol*abs(expected) :
        print("FAIL: ", name, " = ", val, " expected ", expected)
        if feedback_fail != "" :
            print("   ", feedback_fail)
    else :
        print("PASS: ", name, " = ", val, " expected ", expected)
        
def all(env):
    check_close(env["variance_mean_theory"],0.4, "variance_mean_theory", rtol=0.01 ,feedback_fail="3) variance of the mean does not match theory")
    check_close(env["variance_median_theory"],0.628318, "variance_median_theory", rtol=0.01 ,feedback_fail="3) variance of the median does not match theory")
    check_close(env["schechter"](1.5),0.1522, "schechter(1.5)", rtol=0.01 ,feedback_fail="4) schechter(1.5) does not match expected value")
    check_close(env["F"](1.5),0.866282743346153, "F(1.5)", rtol=0.01 ,feedback_fail="5) F(1.5) does not match expected value")
    check_close(env["quantile"](0.5),-0.897930037655197, "quantile(0.5)", rtol=0.01 ,feedback_fail="6) quantile(0.5) does not match expected value")
    check_close(env['mean_x'],1.0, "mean_x", rtol=0.1 ,feedback_fail="8) mean of x estimates does not match expected value")
    check_close(env['bias_x'],0.0, "bias_x", atol=0.01 ,feedback_fail="8) bias of x estimates does not match expected value")
    check_close(env['standard_deviation_x'],0.265501907536280, "standard_deviation_x", rtol=0.1 ,feedback_fail="8) standard deviation of x estimates does not match expected value")
    check_close(env["rank_estimator"](np.arange(0,1,0.01)),0.75, "rank_estimator(np.arange(0,1,0.01))", rtol=0.0,atol=0.0 ,feedback_fail="10) rank_estimator does not match expected value")
    check_close(env["L_star_ave"],13397421052293.846, "L_star_ave" ,feedback_fail="11) L_star_ave does not match expected value")
    check_close(env["mc_variance_data_size"],0.00043768098241664865, "mc_variance_data",rtol=0.2, feedback_fail="12) variance of the MC estimates does not match expected value")
    check_close(env["boot_variance"],8.273417582492536e+22, "boot_variance",rtol=0.1,feedback_fail="13) variance of the bootstrap estimates does not match expected value")