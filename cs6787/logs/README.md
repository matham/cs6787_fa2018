day_test_log_full_11-19_02-16-33.csv, day_log_11-19_02-16-33.csv
Namespace(batch_size=200, cuda=True, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=True, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --rotate_data


day_test_log_full_11-21_23-50-17.csv, day_log_11-21_23-50-17.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.05, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .05

fixed to aplly cw_weight to the original grad of last iter, rather than adjusted grad
day_test_log_full_11-22_00-04-20.csv, day_log_11-22_00-04-20.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.2, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .2

day_test_log_full_11-22_00-13-02.csv, day_log_11-22_00-13-02.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.5, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .5

set the cw_weight to the parameters after the first day
day_test_log_full_11-22_00-17-43.csv, day_log_11-22_00-17-43.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.2, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .2

set momentum to zero after first day
day_test_log_full_11-22_00-33-16.csv, day_log_11-22_00-33-16.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.2, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .2

day_test_log_full_11-23_16-26-49.csv, day_log_11-23_16-26-49.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.5, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .5

day_test_log_full_11-23_16-34-20.csv, day_log_11-23_16-34-20.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.9, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .9

day_test_log_full_11-23_16-42-03.csv, day_log_11-23_16-42-03.csv
Namespace(batch_size=200, cuda=True, cw_weight=2.0, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 2.


day_test_log_full_11-24_23-36-59.csv, log_11-24_23-36-59.csv
Namespace(batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=10, epochs_warm=5, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, warm_epoch_days=30.0)
main.py --cuda --epochs 10 --epoch_days_test 10 --warm_epoch_days 30

day_test_log_full_11-25_00-00-03.csv, log_11-25_00-00-03.csv
Namespace(batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=10, epochs_warm=5, include_invalid=False, lr=0.001, num_hidden_units=2048, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, warm_epoch_days=30.0)
main.py --cuda --epochs 10 --epoch_days_test 10 --warm_epoch_days 30 --num_hidden_units 2048

day_test_log_full_11-25_00-14-28.csv, log_11-25_00-14-28.csv
Namespace(batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=10, epochs_warm=5, include_invalid=False, lr=0.001, num_hidden_units=1024, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, warm_epoch_days=30.0)
main.py --cuda --epochs 10 --epoch_days_test 10 --warm_epoch_days 30 --num_hidden_units 1024

day_test_log_full_11-25_00-18-58.csv, log_11-25_00-18-58.csv
Namespace(batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=20, epochs_warm=5, include_invalid=False, lr=0.001, num_hidden_units=1024, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, warm_epoch_days=30.0)
main.py --cuda --epochs 20 --epoch_days_test 10 --warm_epoch_days 30 --num_hidden_units 1024

day_test_log_full_11-25_00-27-36.csv, log_11-25_00-27-36.csv
Namespace(batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=20, epochs_warm=5, include_invalid=False, lr=0.001, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, warm_epoch_days=30.0)
main.py --cuda --epochs 20 --epoch_days_test 10 --warm_epoch_days 30 --num_hidden_units 512

day_test_log_full_11-25_00-53-06.csv, day_log_11-25_00-53-06.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.31, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_hidden_units=2048, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .31 --num_hidden_units 2048

day_test_log_full_11-25_01-07-55.csv, day_log_11-25_01-07-55.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.31, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .31 --use_last_loss

day_test_log_full_11-25_01-10-58.csv, day_log_11-25_01-10-58.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.31, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .31

day_test_log_full_11-25_02-02-31.csv, day_log_11-25_02-02-31.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=True, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .3 --use_kl_div

day_test_log_full_11-25_02-07-14.csv, day_log_11-25_02-07-14.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=True, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .3 --use_kl_div

day_test_log_full_11-25_02-09-36.csv, day_log_11-25_02-09-36.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=True, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .3 --use_kl_div


day_test_log_full_11-25_19-03-13_False_512.csv, day_log_11-25_19-03-13_False_512.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=100, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .3 --num_hidden_units 512 --use_last_loss --num_day_resample 100

day_test_log_full_11-25_19-03-17_False_512.csv, day_log_11-25_19-03-17_False_512.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=10, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .3 --num_hidden_units 512 --use_last_loss --num_day_resample 10

day_test_log_full_11-25_19-11-47_False_512.csv, day_log_11-25_19-11-47_False_512.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=10, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --num_hidden_units 512 --use_last_loss --num_day_resample 10

day_test_log_full_11-25_19-11-52_False_512.csv, day_log_11-25_19-11-52_False_512.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=100, num_hidden_units=512, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --num_hidden_units 512 --use_last_loss --num_day_resample 100

day_test_log_full_11-25_19-29-07_False_512.csv, day_log_11-25_19-29-07_False_512.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .3 --num_hidden_units 512 --use_last_loss --num_layers 4

day_test_log_full_11-25_19-29-08_False_512.csv, day_log_11-25_19-29-08_False_512.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --num_hidden_units 512 --use_last_loss --num_layers 4

day_test_log_full_11-25_19-41-11.csv, log_11-25_19-41-11.csv
Namespace(batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0.0, epoch_days_test=10.0, epochs=10, epochs_warm=10, include_invalid=False, lr=0.001, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 10 --epoch_days 0 --warm_epoch_days 30 --epochs_warm 10 --num_hidden_units 512 --use_last_loss --num_layers 4 --epoch_days_test 10

day_test_log_full_11-29_23-29-22_2.csv, day_log_11-29_23-29-22_2.csv
Namespace(ae=0.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae .5 --normalize

day_test_log_full_11-29_23-34-31_2.csv, day_log_11-29_23-34-31_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --use_last_loss --normalize

day_test_log_full_11-29_23-37-27_2.csv, day_log_11-29_23-37-27_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.3 --use_last_loss --normalize

day_test_log_full_11-29_23-42-21_2.csv, day_log_11-29_23-42-21_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.3, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=True, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.3 --use_last_loss --normalize --use_kl_div

day_test_log_full_11-29_23-50-38_2.csv, day_log_11-29_23-50-38_2.csv
Namespace(ae=0.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae .9 --normalize

day_test_log_full_11-29_23-51-45_2.csv, day_log_11-29_23-51-45_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.1, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.1 --use_last_loss --normalize

day_test_log_full_11-29_23-59-35_2.csv, day_log_11-29_23-59-35_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --use_last_loss --normalize --num_day_resample 10

day_test_log_full_11-29_23-59-47_2.csv, day_log_11-29_23-59-47_2.csv
Namespace(ae=0.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae .9 --normalize --num_day_resample 10

day_test_log_full_11-30_00-09-14_2.csv, day_log_11-30_00-09-14_2.csv
Namespace(ae=1.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.5 --normalize --num_day_resample 10

day_test_log_full_11-30_00-10-05_2.csv, day_log_11-30_00-10-05_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --use_last_loss --normalize --num_day_resample 5

day_test_log_full_11-30_00-17-09_2.csv, day_log_11-30_00-17-09_2.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=2, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=True, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --use_last_loss --normalize --num_day_resample 2

day_test_log_full_11-30_00-17-16_2.csv, day_log_11-30_00-17-16_2.csv
Namespace(ae=1.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.5 --normalize --num_day_resample 5


day_test_log_full_11-30_00-24-32_2.csv, day_log_11-30_00-24-32_2.csv
Namespace(ae=5.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 5 --normalize

day_test_log_full_11-30_00-25-42_2.csv, day_log_11-30_00-25-42_2.csv
Namespace(ae=1.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=2, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.5 --normalize --num_day_resample 2

day_test_log_full_11-30_00-29-49_2.csv, day_log_11-30_00-29-49_2.csv
Namespace(ae=4.0, batch_size=200, cuda=True, cw_weight=0.0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight 0.0 --ae 4 --normalize --num_day_resample 5


day_test_log_full_12-01_16-40-21_False_0.csv, day_log_12-01_16-40-21_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.00 --normalize

day_test_log_full_12-01_16-40-34_True_1.csv, day_log_12-01_16-40-34_True_1.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 1

day_test_log_full_12-01_16-46-59_True_0.csv, day_log_12-01_16-46-59_True_0.csv
Namespace(ae=0.02, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.02 --normalize

day_test_log_full_12-01_16-48-48_True_0.csv, day_log_12-01_16-48-48_True_0.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 0

day_test_log_full_12-01_16-54-46_True_0.csv, day_log_12-01_16-54-46_True_0.csv
Namespace(ae=0.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.04 --normalize

day_test_log_full_12-01_16-57-24_True_3.csv, day_log_12-01_16-57-24_True_3.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 3

day_test_log_full_12-01_17-02-25_True_0.csv, day_log_12-01_17-02-25_True_0.csv
Namespace(ae=0.06, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.06 --normalize

day_test_log_full_12-01_17-06-07_True_5.csv, day_log_12-01_17-06-07_True_5.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 5

day_test_log_full_12-01_17-10-30_True_0.csv, day_log_12-01_17-10-30_True_0.csv
Namespace(ae=0.08, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.08 --normalize

day_test_log_full_12-01_17-13-58_True_10.csv, day_log_12-01_17-13-58_True_10.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 10

day_test_log_full_12-01_17-18-16_True_0.csv, day_log_12-01_17-18-16_True_0.csv
Namespace(ae=0.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.10 --normalize

day_test_log_full_12-01_17-22-45_True_50.csv, day_log_12-01_17-22-45_True_50.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 50

day_test_log_full_12-01_17-26-17_True_0.csv, day_log_12-01_17-26-17_True_0.csv
Namespace(ae=0.12, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.12 --normalize

day_test_log_full_12-01_17-31-54_True_100.csv, day_log_12-01_17-31-54_True_100.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 100

day_test_log_full_12-01_17-34-37_True_0.csv, day_log_12-01_17-34-37_True_0.csv
Namespace(ae=0.14, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.14 --normalize

day_test_log_full_12-01_17-40-57_True_1.csv, day_log_12-01_17-40-57_True_1.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 1

day_test_log_full_12-01_17-43-21_True_0.csv, day_log_12-01_17-43-21_True_0.csv
Namespace(ae=0.16, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.16 --normalize

day_test_log_full_12-01_17-50-05_True_0.csv, day_log_12-01_17-50-05_True_0.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 0

day_test_log_full_12-01_17-52-21_True_0.csv, day_log_12-01_17-52-21_True_0.csv
Namespace(ae=0.18, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.18 --normalize

day_test_log_full_12-01_17-57-42_True_3.csv, day_log_12-01_17-57-42_True_3.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 3

day_test_log_full_12-01_18-00-56_True_0.csv, day_log_12-01_18-00-56_True_0.csv
Namespace(ae=0.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.20 --normalize

day_test_log_full_12-01_18-05-53_True_5.csv, day_log_12-01_18-05-53_True_5.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 5

day_test_log_full_12-01_18-08-39_True_0.csv, day_log_12-01_18-08-39_True_0.csv
Namespace(ae=0.22, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.22 --normalize

day_test_log_full_12-01_18-14-44_True_10.csv, day_log_12-01_18-14-44_True_10.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 10

day_test_log_full_12-01_18-16-47_True_0.csv, day_log_12-01_18-16-47_True_0.csv
Namespace(ae=0.24, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.24 --normalize

day_test_log_full_12-01_18-22-48_True_50.csv, day_log_12-01_18-22-48_True_50.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 50

day_test_log_full_12-01_18-24-35_True_0.csv, day_log_12-01_18-24-35_True_0.csv
Namespace(ae=0.26, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.26 --normalize

day_test_log_full_12-01_18-31-48_True_100.csv, day_log_12-01_18-31-48_True_100.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 100

day_test_log_full_12-01_18-32-26_True_0.csv, day_log_12-01_18-32-26_True_0.csv
Namespace(ae=0.28, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.28 --normalize

day_test_log_full_12-01_18-40-17_True_1.csv, day_log_12-01_18-40-17_True_1.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 1

day_test_log_full_12-01_18-40-39_True_0.csv, day_log_12-01_18-40-39_True_0.csv
Namespace(ae=0.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.30 --normalize

day_test_log_full_12-01_18-48-46_True_0.csv, day_log_12-01_18-48-46_True_0.csv
Namespace(ae=0.32, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.32 --normalize

day_test_log_full_12-01_18-49-01_True_0.csv, day_log_12-01_18-49-01_True_0.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 0

day_test_log_full_12-01_18-57-06_True_0.csv, day_log_12-01_18-57-06_True_0.csv
Namespace(ae=0.34, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.34 --normalize

day_test_log_full_12-01_18-57-33_True_3.csv, day_log_12-01_18-57-33_True_3.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 3

day_test_log_full_12-01_19-05-01_True_0.csv, day_log_12-01_19-05-01_True_0.csv
Namespace(ae=0.36, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.36 --normalize

day_test_log_full_12-01_19-05-51_True_5.csv, day_log_12-01_19-05-51_True_5.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 5

day_test_log_full_12-01_19-13-58_True_0.csv, day_log_12-01_19-13-58_True_0.csv
Namespace(ae=0.38, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.38 --normalize

day_test_log_full_12-01_19-14-04_True_10.csv, day_log_12-01_19-14-04_True_10.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 10

day_test_log_full_12-01_19-22-18_True_50.csv, day_log_12-01_19-22-18_True_50.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 50

day_test_log_full_12-01_19-22-27_True_0.csv, day_log_12-01_19-22-27_True_0.csv
Namespace(ae=0.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.40 --normalize

day_test_log_full_12-01_19-30-16_True_0.csv, day_log_12-01_19-30-16_True_0.csv
Namespace(ae=0.42, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.42 --normalize

day_test_log_full_12-01_19-31-00_True_100.csv, day_log_12-01_19-31-00_True_100.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 100

day_test_log_full_12-01_19-38-48_True_0.csv, day_log_12-01_19-38-48_True_0.csv
Namespace(ae=0.44, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.44 --normalize

day_test_log_full_12-01_19-39-26_True_1.csv, day_log_12-01_19-39-26_True_1.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 1

day_test_log_full_12-01_19-46-28_True_0.csv, day_log_12-01_19-46-28_True_0.csv
Namespace(ae=0.46, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.46 --normalize

day_test_log_full_12-01_19-48-00_True_0.csv, day_log_12-01_19-48-00_True_0.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 0

day_test_log_full_12-01_19-55-21_True_0.csv, day_log_12-01_19-55-21_True_0.csv
Namespace(ae=0.48, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.48 --normalize

day_test_log_full_12-01_19-55-53_True_3.csv, day_log_12-01_19-55-53_True_3.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 3

day_test_log_full_12-01_20-03-53_True_5.csv, day_log_12-01_20-03-53_True_5.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 5

day_test_log_full_12-01_20-04-04_True_0.csv, day_log_12-01_20-04-04_True_0.csv
Namespace(ae=0.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.50 --normalize

day_test_log_full_12-01_20-12-14_True_0.csv, day_log_12-01_20-12-14_True_0.csv
Namespace(ae=0.52, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.52 --normalize

day_test_log_full_12-01_20-12-45_True_10.csv, day_log_12-01_20-12-45_True_10.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 10

day_test_log_full_12-01_20-20-48_True_0.csv, day_log_12-01_20-20-48_True_0.csv
Namespace(ae=0.54, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.54 --normalize

day_test_log_full_12-01_20-21-38_True_50.csv, day_log_12-01_20-21-38_True_50.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 50

day_test_log_full_12-01_20-29-03_True_0.csv, day_log_12-01_20-29-03_True_0.csv
Namespace(ae=0.56, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.56 --normalize

day_test_log_full_12-01_20-29-41_True_100.csv, day_log_12-01_20-29-41_True_100.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 100

day_test_log_full_12-01_20-37-54_True_1.csv, day_log_12-01_20-37-54_True_1.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 1

day_test_log_full_12-01_20-38-11_True_0.csv, day_log_12-01_20-38-11_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize

day_test_log_full_12-01_20-46-45_True_0.csv, day_log_12-01_20-46-45_True_0.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 0

day_test_log_full_12-01_20-47-11_True_0.csv, day_log_12-01_20-47-11_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize

day_test_log_full_12-01_20-54-49_True_3.csv, day_log_12-01_20-54-49_True_3.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 3

day_test_log_full_12-01_20-55-01_True_0.csv, day_log_12-01_20-55-01_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize

day_test_log_full_12-01_21-03-24_True_0.csv, day_log_12-01_21-03-24_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize

day_test_log_full_12-01_21-04-04_True_5.csv, day_log_12-01_21-04-04_True_5.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 5

day_test_log_full_12-01_21-12-13_True_0.csv, day_log_12-01_21-12-13_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize

day_test_log_full_12-01_21-13-08_True_10.csv, day_log_12-01_21-13-08_True_10.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .75 --num_day_resample 10

day_test_log_full_12-01_21-21-11_True_0.csv, day_log_12-01_21-21-11_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize

day_test_log_full_12-01_21-41-20_False_0.csv, day_log_12-01_21-41-20_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.00 --normalize

day_test_log_full_12-01_21-49-39_True_0.csv, day_log_12-01_21-49-39_True_0.csv
Namespace(ae=0.02, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.02 --normalize

day_test_log_full_12-01_21-58-41_True_0.csv, day_log_12-01_21-58-41_True_0.csv
Namespace(ae=0.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.04 --normalize

day_test_log_full_12-01_22-06-54_True_0.csv, day_log_12-01_22-06-54_True_0.csv
Namespace(ae=0.06, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.06 --normalize

day_test_log_full_12-01_22-15-06_True_0.csv, day_log_12-01_22-15-06_True_0.csv
Namespace(ae=0.08, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.08 --normalize

day_test_log_full_12-01_22-24-12_True_0.csv, day_log_12-01_22-24-12_True_0.csv
Namespace(ae=0.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.10 --normalize

day_test_log_full_12-01_22-33-14_True_0.csv, day_log_12-01_22-33-14_True_0.csv
Namespace(ae=0.12, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.12 --normalize

day_test_log_full_12-01_22-42-15_True_0.csv, day_log_12-01_22-42-15_True_0.csv
Namespace(ae=0.14, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.14 --normalize

day_test_log_full_12-01_22-50-40_True_0.csv, day_log_12-01_22-50-40_True_0.csv
Namespace(ae=0.16, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.16 --normalize

day_test_log_full_12-01_22-59-29_True_0.csv, day_log_12-01_22-59-29_True_0.csv
Namespace(ae=0.18, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.18 --normalize

day_test_log_full_12-01_23-08-24_True_0.csv, day_log_12-01_23-08-24_True_0.csv
Namespace(ae=0.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.20 --normalize

day_test_log_full_12-01_23-17-12_True_0.csv, day_log_12-01_23-17-12_True_0.csv
Namespace(ae=0.22, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.22 --normalize

day_test_log_full_12-01_23-25-28_True_0.csv, day_log_12-01_23-25-28_True_0.csv
Namespace(ae=0.24, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.24 --normalize

day_test_log_full_12-01_23-33-56_True_0.csv, day_log_12-01_23-33-56_True_0.csv
Namespace(ae=0.26, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.26 --normalize

day_test_log_full_12-01_23-42-06_True_0.csv, day_log_12-01_23-42-06_True_0.csv
Namespace(ae=0.28, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.28 --normalize

day_test_log_full_12-01_23-51-14_True_0.csv, day_log_12-01_23-51-14_True_0.csv
Namespace(ae=0.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.30 --normalize

day_test_log_full_12-02_00-00-08_True_0.csv, day_log_12-02_00-00-08_True_0.csv
Namespace(ae=0.32, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.32 --normalize

day_test_log_full_12-02_00-09-10_True_0.csv, day_log_12-02_00-09-10_True_0.csv
Namespace(ae=0.34, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.34 --normalize

day_test_log_full_12-02_00-17-53_True_0.csv, day_log_12-02_00-17-53_True_0.csv
Namespace(ae=0.36, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.36 --normalize

day_test_log_full_12-02_00-26-59_True_0.csv, day_log_12-02_00-26-59_True_0.csv
Namespace(ae=0.38, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.38 --normalize

day_test_log_full_12-02_00-36-01_True_0.csv, day_log_12-02_00-36-01_True_0.csv
Namespace(ae=0.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.40 --normalize

day_test_log_full_12-02_00-45-00_True_0.csv, day_log_12-02_00-45-00_True_0.csv
Namespace(ae=0.42, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.42 --normalize

day_test_log_full_12-02_00-54-03_True_0.csv, day_log_12-02_00-54-03_True_0.csv
Namespace(ae=0.44, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.44 --normalize

day_test_log_full_12-02_01-02-52_True_0.csv, day_log_12-02_01-02-52_True_0.csv
Namespace(ae=0.46, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.46 --normalize

day_test_log_full_12-02_01-11-13_True_0.csv, day_log_12-02_01-11-13_True_0.csv
Namespace(ae=0.48, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.48 --normalize

day_test_log_full_12-02_01-19-32_True_0.csv, day_log_12-02_01-19-32_True_0.csv
Namespace(ae=0.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.50 --normalize

day_test_log_full_12-02_01-28-30_True_0.csv, day_log_12-02_01-28-30_True_0.csv
Namespace(ae=0.52, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.52 --normalize

day_test_log_full_12-02_01-37-34_True_0.csv, day_log_12-02_01-37-34_True_0.csv
Namespace(ae=0.54, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.54 --normalize

day_test_log_full_12-02_01-46-38_True_0.csv, day_log_12-02_01-46-38_True_0.csv
Namespace(ae=0.56, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.56 --normalize

day_test_log_full_12-02_01-55-39_True_0.csv, day_log_12-02_01-55-39_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize

day_test_log_full_12-02_02-03-59_True_0.csv, day_log_12-02_02-03-59_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize

day_test_log_full_12-02_02-12-13_True_0.csv, day_log_12-02_02-12-13_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize

day_test_log_full_12-02_02-21-21_True_0.csv, day_log_12-02_02-21-21_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize

day_test_log_full_12-02_02-30-25_True_0.csv, day_log_12-02_02-30-25_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize

day_test_log_full_12-02_02-39-16_True_0.csv, day_log_12-02_02-39-16_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize

day_test_log_full_12-02_02-47-37_True_0.csv, day_log_12-02_02-47-37_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize

day_test_log_full_12-02_02-56-00_True_0.csv, day_log_12-02_02-56-00_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize

day_test_log_full_12-02_03-05-00_True_0.csv, day_log_12-02_03-05-00_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize

day_test_log_full_12-02_03-14-09_True_0.csv, day_log_12-02_03-14-09_True_0.csv
Namespace(ae=0.76, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.76 --normalize

day_test_log_full_12-02_03-23-11_True_0.csv, day_log_12-02_03-23-11_True_0.csv
Namespace(ae=0.78, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.78 --normalize

day_test_log_full_12-02_03-31-41_True_0.csv, day_log_12-02_03-31-41_True_0.csv
Namespace(ae=0.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.80 --normalize

day_test_log_full_12-02_03-40-27_True_0.csv, day_log_12-02_03-40-27_True_0.csv
Namespace(ae=0.82, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.82 --normalize

day_test_log_full_12-02_03-48-50_True_0.csv, day_log_12-02_03-48-50_True_0.csv
Namespace(ae=0.84, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.84 --normalize

day_test_log_full_12-02_03-57-13_True_0.csv, day_log_12-02_03-57-13_True_0.csv
Namespace(ae=0.86, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.86 --normalize

day_test_log_full_12-02_04-05-53_True_0.csv, day_log_12-02_04-05-53_True_0.csv
Namespace(ae=0.88, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.88 --normalize

day_test_log_full_12-02_04-14-36_True_0.csv, day_log_12-02_04-14-36_True_0.csv
Namespace(ae=0.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.90 --normalize

day_test_log_full_12-02_04-23-02_True_0.csv, day_log_12-02_04-23-02_True_0.csv
Namespace(ae=0.92, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.92 --normalize

day_test_log_full_12-02_04-31-48_True_0.csv, day_log_12-02_04-31-48_True_0.csv
Namespace(ae=0.94, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.94 --normalize

day_test_log_full_12-02_04-40-27_True_0.csv, day_log_12-02_04-40-27_True_0.csv
Namespace(ae=0.96, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.96 --normalize

day_test_log_full_12-02_04-48-50_True_0.csv, day_log_12-02_04-48-50_True_0.csv
Namespace(ae=0.98, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.98 --normalize

day_test_log_full_12-02_04-57-34_True_0.csv, day_log_12-02_04-57-34_True_0.csv
Namespace(ae=1.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.00 --normalize

day_test_log_full_12-02_05-06-07_True_0.csv, day_log_12-02_05-06-07_True_0.csv
Namespace(ae=1.02, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.02 --normalize

day_test_log_full_12-02_05-14-22_True_0.csv, day_log_12-02_05-14-22_True_0.csv
Namespace(ae=1.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.04 --normalize

day_test_log_full_12-02_05-23-21_True_0.csv, day_log_12-02_05-23-21_True_0.csv
Namespace(ae=1.06, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.06 --normalize

day_test_log_full_12-02_05-31-37_True_0.csv, day_log_12-02_05-31-37_True_0.csv
Namespace(ae=1.08, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.08 --normalize

day_test_log_full_12-02_05-40-14_True_0.csv, day_log_12-02_05-40-14_True_0.csv
Namespace(ae=1.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.10 --normalize

day_test_log_full_12-02_05-48-32_True_0.csv, day_log_12-02_05-48-32_True_0.csv
Namespace(ae=1.12, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.12 --normalize

day_test_log_full_12-02_05-56-44_True_0.csv, day_log_12-02_05-56-44_True_0.csv
Namespace(ae=1.14, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.14 --normalize

day_test_log_full_12-02_06-05-08_True_0.csv, day_log_12-02_06-05-08_True_0.csv
Namespace(ae=1.16, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.16 --normalize

day_test_log_full_12-02_06-14-12_True_0.csv, day_log_12-02_06-14-12_True_0.csv
Namespace(ae=1.18, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.18 --normalize

day_test_log_full_12-02_06-22-56_True_0.csv, day_log_12-02_06-22-56_True_0.csv
Namespace(ae=1.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.20 --normalize

day_test_log_full_12-02_06-31-14_True_0.csv, day_log_12-02_06-31-14_True_0.csv
Namespace(ae=1.22, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.22 --normalize

day_test_log_full_12-02_06-39-55_True_0.csv, day_log_12-02_06-39-55_True_0.csv
Namespace(ae=1.24, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.24 --normalize

day_test_log_full_12-02_06-48-55_True_0.csv, day_log_12-02_06-48-55_True_0.csv
Namespace(ae=1.26, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.26 --normalize

day_test_log_full_12-02_06-58-02_True_0.csv, day_log_12-02_06-58-02_True_0.csv
Namespace(ae=1.28, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.28 --normalize

day_test_log_full_12-02_07-07-04_True_0.csv, day_log_12-02_07-07-04_True_0.csv
Namespace(ae=1.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.30 --normalize

day_test_log_full_12-02_07-16-07_True_0.csv, day_log_12-02_07-16-07_True_0.csv
Namespace(ae=1.32, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.32 --normalize

day_test_log_full_12-02_07-25-07_True_0.csv, day_log_12-02_07-25-07_True_0.csv
Namespace(ae=1.34, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.34 --normalize

day_test_log_full_12-02_07-34-23_True_0.csv, day_log_12-02_07-34-23_True_0.csv
Namespace(ae=1.36, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.36 --normalize

day_test_log_full_12-02_07-42-47_True_0.csv, day_log_12-02_07-42-47_True_0.csv
Namespace(ae=1.38, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.38 --normalize

day_test_log_full_12-02_07-51-03_True_0.csv, day_log_12-02_07-51-03_True_0.csv
Namespace(ae=1.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.40 --normalize

day_test_log_full_12-02_07-59-39_True_0.csv, day_log_12-02_07-59-39_True_0.csv
Namespace(ae=1.42, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.42 --normalize

day_test_log_full_12-02_08-08-22_True_0.csv, day_log_12-02_08-08-22_True_0.csv
Namespace(ae=1.44, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.44 --normalize

day_test_log_full_12-02_08-17-00_True_0.csv, day_log_12-02_08-17-00_True_0.csv
Namespace(ae=1.46, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.46 --normalize

day_test_log_full_12-02_08-25-41_True_0.csv, day_log_12-02_08-25-41_True_0.csv
Namespace(ae=1.48, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.48 --normalize

day_test_log_full_12-02_08-34-41_True_0.csv, day_log_12-02_08-34-41_True_0.csv
Namespace(ae=1.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.50 --normalize

day_test_log_full_12-02_08-43-43_False_0.csv, day_log_12-02_08-43-43_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.00 --normalize

day_test_log_full_12-02_08-52-06_True_0.csv, day_log_12-02_08-52-06_True_0.csv
Namespace(ae=0.02, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.02 --normalize

day_test_log_full_12-02_09-00-50_True_0.csv, day_log_12-02_09-00-50_True_0.csv
Namespace(ae=0.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.04 --normalize

day_test_log_full_12-02_09-09-18_True_0.csv, day_log_12-02_09-09-18_True_0.csv
Namespace(ae=0.06, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.06 --normalize

day_test_log_full_12-02_09-18-15_True_0.csv, day_log_12-02_09-18-15_True_0.csv
Namespace(ae=0.08, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.08 --normalize

day_test_log_full_12-02_09-26-54_True_0.csv, day_log_12-02_09-26-54_True_0.csv
Namespace(ae=0.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.10 --normalize

day_test_log_full_12-02_09-35-37_True_0.csv, day_log_12-02_09-35-37_True_0.csv
Namespace(ae=0.12, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.12 --normalize

day_test_log_full_12-02_09-43-55_True_0.csv, day_log_12-02_09-43-55_True_0.csv
Namespace(ae=0.14, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.14 --normalize

day_test_log_full_12-02_09-52-27_True_0.csv, day_log_12-02_09-52-27_True_0.csv
Namespace(ae=0.16, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.16 --normalize

day_test_log_full_12-02_10-00-50_True_0.csv, day_log_12-02_10-00-50_True_0.csv
Namespace(ae=0.18, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.18 --normalize

day_test_log_full_12-02_10-09-25_True_0.csv, day_log_12-02_10-09-25_True_0.csv
Namespace(ae=0.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.20 --normalize

day_test_log_full_12-02_10-17-53_True_0.csv, day_log_12-02_10-17-53_True_0.csv
Namespace(ae=0.22, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.22 --normalize

day_test_log_full_12-02_10-26-16_True_0.csv, day_log_12-02_10-26-16_True_0.csv
Namespace(ae=0.24, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.24 --normalize

day_test_log_full_12-02_10-34-41_True_0.csv, day_log_12-02_10-34-41_True_0.csv
Namespace(ae=0.26, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.26 --normalize

day_test_log_full_12-02_10-43-45_True_0.csv, day_log_12-02_10-43-45_True_0.csv
Namespace(ae=0.28, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.28 --normalize

day_test_log_full_12-02_10-52-49_True_0.csv, day_log_12-02_10-52-49_True_0.csv
Namespace(ae=0.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.30 --normalize

day_test_log_full_12-02_11-01-43_True_0.csv, day_log_12-02_11-01-43_True_0.csv
Namespace(ae=0.32, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.32 --normalize

day_test_log_full_12-02_11-10-32_True_0.csv, day_log_12-02_11-10-32_True_0.csv
Namespace(ae=0.34, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.34 --normalize

day_test_log_full_12-02_11-18-49_True_0.csv, day_log_12-02_11-18-49_True_0.csv
Namespace(ae=0.36, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.36 --normalize

day_test_log_full_12-02_11-27-10_True_0.csv, day_log_12-02_11-27-10_True_0.csv
Namespace(ae=0.38, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.38 --normalize

day_test_log_full_12-02_11-35-30_True_0.csv, day_log_12-02_11-35-30_True_0.csv
Namespace(ae=0.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.40 --normalize

day_test_log_full_12-02_11-44-26_True_0.csv, day_log_12-02_11-44-26_True_0.csv
Namespace(ae=0.42, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.42 --normalize

day_test_log_full_12-02_11-53-26_True_0.csv, day_log_12-02_11-53-26_True_0.csv
Namespace(ae=0.44, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.44 --normalize

day_test_log_full_12-02_12-02-27_True_0.csv, day_log_12-02_12-02-27_True_0.csv
Namespace(ae=0.46, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.46 --normalize

day_test_log_full_12-02_12-11-31_True_0.csv, day_log_12-02_12-11-31_True_0.csv
Namespace(ae=0.48, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.48 --normalize

day_test_log_full_12-02_12-20-20_True_0.csv, day_log_12-02_12-20-20_True_0.csv
Namespace(ae=0.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.50 --normalize

day_test_log_full_12-02_12-28-53_True_0.csv, day_log_12-02_12-28-53_True_0.csv
Namespace(ae=0.52, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.52 --normalize

day_test_log_full_12-02_12-37-56_True_0.csv, day_log_12-02_12-37-56_True_0.csv
Namespace(ae=0.54, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.54 --normalize

day_test_log_full_12-02_12-46-58_True_0.csv, day_log_12-02_12-46-58_True_0.csv
Namespace(ae=0.56, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.56 --normalize

day_test_log_full_12-02_12-56-08_True_0.csv, day_log_12-02_12-56-08_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize

day_test_log_full_12-02_13-05-19_True_0.csv, day_log_12-02_13-05-19_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize

day_test_log_full_12-02_13-13-58_True_0.csv, day_log_12-02_13-13-58_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize

day_test_log_full_12-02_13-22-50_True_0.csv, day_log_12-02_13-22-50_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize

day_test_log_full_12-02_13-31-26_True_0.csv, day_log_12-02_13-31-26_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize

day_test_log_full_12-02_13-39-48_True_0.csv, day_log_12-02_13-39-48_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize

day_test_log_full_12-02_13-48-50_True_0.csv, day_log_12-02_13-48-50_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize

day_test_log_full_12-02_13-57-41_True_0.csv, day_log_12-02_13-57-41_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize

day_test_log_full_12-02_14-06-43_True_0.csv, day_log_12-02_14-06-43_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize

day_test_log_full_12-02_14-15-48_True_0.csv, day_log_12-02_14-15-48_True_0.csv
Namespace(ae=0.76, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.76 --normalize

day_test_log_full_12-02_14-25-01_True_0.csv, day_log_12-02_14-25-01_True_0.csv
Namespace(ae=0.78, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.78 --normalize

day_test_log_full_12-02_14-34-04_True_0.csv, day_log_12-02_14-34-04_True_0.csv
Namespace(ae=0.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.80 --normalize

day_test_log_full_12-02_14-43-18_True_0.csv, day_log_12-02_14-43-18_True_0.csv
Namespace(ae=0.82, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.82 --normalize

day_test_log_full_12-02_14-52-22_True_0.csv, day_log_12-02_14-52-22_True_0.csv
Namespace(ae=0.84, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.84 --normalize

day_test_log_full_12-02_15-01-38_True_0.csv, day_log_12-02_15-01-38_True_0.csv
Namespace(ae=0.86, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.86 --normalize

day_test_log_full_12-02_15-10-51_True_0.csv, day_log_12-02_15-10-51_True_0.csv
Namespace(ae=0.88, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.88 --normalize

day_test_log_full_12-02_15-20-07_True_0.csv, day_log_12-02_15-20-07_True_0.csv
Namespace(ae=0.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.90 --normalize

day_test_log_full_12-02_15-29-26_True_0.csv, day_log_12-02_15-29-26_True_0.csv
Namespace(ae=0.92, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.92 --normalize

day_test_log_full_12-02_15-38-52_True_0.csv, day_log_12-02_15-38-52_True_0.csv
Namespace(ae=0.94, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.94 --normalize

day_test_log_full_12-02_15-48-18_True_0.csv, day_log_12-02_15-48-18_True_0.csv
Namespace(ae=0.96, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.96 --normalize

day_test_log_full_12-02_15-57-54_True_0.csv, day_log_12-02_15-57-54_True_0.csv
Namespace(ae=0.98, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.98 --normalize

day_test_log_full_12-02_16-07-22_True_0.csv, day_log_12-02_16-07-22_True_0.csv
Namespace(ae=1.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.00 --normalize

day_test_log_full_12-02_16-16-56_True_0.csv, day_log_12-02_16-16-56_True_0.csv
Namespace(ae=1.02, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.02 --normalize

day_test_log_full_12-02_16-26-32_True_0.csv, day_log_12-02_16-26-32_True_0.csv
Namespace(ae=1.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.04 --normalize

day_test_log_full_12-02_16-35-57_True_0.csv, day_log_12-02_16-35-57_True_0.csv
Namespace(ae=1.06, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.06 --normalize

day_test_log_full_12-02_16-45-20_True_0.csv, day_log_12-02_16-45-20_True_0.csv
Namespace(ae=1.08, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.08 --normalize

day_test_log_full_12-02_16-54-48_True_0.csv, day_log_12-02_16-54-48_True_0.csv
Namespace(ae=1.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.10 --normalize

day_test_log_full_12-02_17-04-15_True_0.csv, day_log_12-02_17-04-15_True_0.csv
Namespace(ae=1.12, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.12 --normalize

day_test_log_full_12-02_17-13-52_True_0.csv, day_log_12-02_17-13-52_True_0.csv
Namespace(ae=1.14, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.14 --normalize

day_test_log_full_12-02_17-16-11_True_0.csv, day_log_12-02_17-16-11_True_0.csv
Namespace(ae=1.16, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 1.16 --normalize

day_test_log_full_12-02_17-16-57_False_0.csv, day_log_12-02_17-16-57_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.00 --normalize

day_test_log_full_12-02_17-25-51_True_0.csv, day_log_12-02_17-25-51_True_0.csv
Namespace(ae=0.02, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.02 --normalize

day_test_log_full_12-02_17-34-57_True_0.csv, day_log_12-02_17-34-57_True_0.csv
Namespace(ae=0.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.04 --normalize

day_test_log_full_12-02_17-40-32_True_0.csv, day_log_12-02_17-40-32_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize

day_test_log_full_12-02_17-49-58_True_0.csv, day_log_12-02_17-49-58_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize

day_test_log_full_12-02_17-58-47_True_0.csv, day_log_12-02_17-58-47_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize

day_test_log_full_12-02_17-59-39_True_1.csv, day_log_12-02_17-59-39_True_1.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 1 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-07-32_True_0.csv, day_log_12-02_18-07-32_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 0 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-07-48_True_0.csv, day_log_12-02_18-07-48_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize

day_test_log_full_12-02_18-07-53_False_0.csv, day_log_12-02_18-07-53_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_18-15-25_True_0.csv, day_log_12-02_18-15-25_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_18-15-26_True_3.csv, day_log_12-02_18-15-26_True_3.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 3 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-16-49_True_0.csv, day_log_12-02_18-16-49_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize

day_test_log_full_12-02_18-24-19_False_0.csv, day_log_12-02_18-24-19_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_18-24-41_True_5.csv, day_log_12-02_18-24-41_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 5 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-26-06_True_0.csv, day_log_12-02_18-26-06_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize

day_test_log_full_12-02_18-31-44_True_0.csv, day_log_12-02_18-31-44_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_18-34-03_True_10.csv, day_log_12-02_18-34-03_True_10.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 10 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-35-49_True_0.csv, day_log_12-02_18-35-49_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize

day_test_log_full_12-02_18-40-46_False_0.csv, day_log_12-02_18-40-46_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_18-43-24_True_50.csv, day_log_12-02_18-43-24_True_50.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 50 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-45-24_True_0.csv, day_log_12-02_18-45-24_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize

day_test_log_full_12-02_18-49-08_True_0.csv, day_log_12-02_18-49-08_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_18-52-50_True_100.csv, day_log_12-02_18-52-50_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 100 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_18-54-58_True_0.csv, day_log_12-02_18-54-58_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize

day_test_log_full_12-02_18-58-00_False_0.csv, day_log_12-02_18-58-00_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_19-02-29_True_1.csv, day_log_12-02_19-02-29_True_1.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 1 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_19-06-07_True_0.csv, day_log_12-02_19-06-07_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_19-12-07_True_0.csv, day_log_12-02_19-12-07_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 0 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_19-15-53_False_0.csv, day_log_12-02_19-15-53_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_19-21-44_True_3.csv, day_log_12-02_19-21-44_True_3.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 3 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_19-24-51_True_0.csv, day_log_12-02_19-24-51_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_19-25-08_True_0.csv, day_log_12-02_19-25-08_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_19-31-32_True_5.csv, day_log_12-02_19-31-32_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 5 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_19-34-14_True_0.csv, day_log_12-02_19-34-14_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_19-34-47_False_0.csv, day_log_12-02_19-34-47_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_19-41-29_True_10.csv, day_log_12-02_19-41-29_True_10.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 10 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_19-43-39_True_0.csv, day_log_12-02_19-43-39_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_19-43-40_True_0.csv, day_log_12-02_19-43-40_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_19-51-02_True_50.csv, day_log_12-02_19-51-02_True_50.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 50 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_19-52-43_True_0.csv, day_log_12-02_19-52-43_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_19-53-20_False_0.csv, day_log_12-02_19-53-20_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_19-58-06_False_0.csv, day_log_12-02_19-58-06_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-00-54_True_100.csv, day_log_12-02_20-00-54_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 100 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-01-58_True_0.csv, day_log_12-02_20-01-58_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_20-02-14_True_0.csv, day_log_12-02_20-02-14_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_20-05-40_False_0.csv, day_log_12-02_20-05-40_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-05-42_True_0.csv, day_log_12-02_20-05-42_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-11-21_True_1.csv, day_log_12-02_20-11-21_True_1.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 1 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-11-50_True_0.csv, day_log_12-02_20-11-50_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_20-12-35_False_0.csv, day_log_12-02_20-12-35_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_20-14-55_False_0.csv, day_log_12-02_20-14-55_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-15-19_False_0.csv, day_log_12-02_20-15-19_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-21-42_True_0.csv, day_log_12-02_20-21-42_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_20-21-50_True_0.csv, day_log_12-02_20-21-50_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 0 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-21-51_True_0.csv, day_log_12-02_20-21-51_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_20-23-33_True_0.csv, day_log_12-02_20-23-33_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-24-29_False_0.csv, day_log_12-02_20-24-29_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-31-23_False_0.csv, day_log_12-02_20-31-23_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_20-31-36_True_3.csv, day_log_12-02_20-31-36_True_3.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 3 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-31-53_True_0.csv, day_log_12-02_20-31-53_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_20-32-21_False_0.csv, day_log_12-02_20-32-21_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-32-32_False_0.csv, day_log_12-02_20-32-32_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-39-47_True_0.csv, day_log_12-02_20-39-47_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_20-40-30_False_0.csv, day_log_12-02_20-40-30_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-40-47_True_0.csv, day_log_12-02_20-40-47_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-40-51_True_5.csv, day_log_12-02_20-40-51_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 5 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-41-47_True_0.csv, day_log_12-02_20-41-47_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_2', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_2

day_test_log_full_12-02_20-49-14_False_0.csv, day_log_12-02_20-49-14_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-49-53_False_0.csv, day_log_12-02_20-49-53_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_20-50-05_True_10.csv, day_log_12-02_20-50-05_True_10.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 10 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-50-31_True_0.csv, day_log_12-02_20-50-31_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_20-51-01_False_0.csv, day_log_12-02_20-51-01_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_20-58-37_False_0.csv, day_log_12-02_20-58-37_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_20-58-50_True_0.csv, day_log_12-02_20-58-50_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_20-59-15_True_0.csv, day_log_12-02_20-59-15_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_20-59-29_True_50.csv, day_log_12-02_20-59-29_True_50.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 50 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_20-59-46_True_0.csv, day_log_12-02_20-59-46_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-08-32_False_0.csv, day_log_12-02_21-08-32_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_21-08-46_False_0.csv, day_log_12-02_21-08-46_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_21-08-46_True_0.csv, day_log_12-02_21-08-46_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_21-09-02_True_100.csv, day_log_12-02_21-09-02_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 100 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_21-09-54_False_0.csv, day_log_12-02_21-09-54_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-17-12_False_0.csv, day_log_12-02_21-17-12_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_21-17-34_True_0.csv, day_log_12-02_21-17-34_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_21-18-35_True_0.csv, day_log_12-02_21-18-35_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_21-18-35_True_0.csv, day_log_12-02_21-18-35_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-18-48_True_1.csv, day_log_12-02_21-18-48_True_1.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 1 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_21-26-04_False_0.csv, day_log_12-02_21-26-04_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_21-27-52_False_0.csv, day_log_12-02_21-27-52_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_21-28-32_True_0.csv, day_log_12-02_21-28-32_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 0 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_21-28-58_False_0.csv, day_log_12-02_21-28-58_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-29-01_True_0.csv, day_log_12-02_21-29-01_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_21-35-45_False_0.csv, day_log_12-02_21-35-45_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_21-36-46_True_0.csv, day_log_12-02_21-36-46_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_21-37-48_True_0.csv, day_log_12-02_21-37-48_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-38-15_True_3.csv, day_log_12-02_21-38-15_True_3.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 3 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_21-39-05_True_0.csv, day_log_12-02_21-39-05_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_21-45-31_False_0.csv, day_log_12-02_21-45-31_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_21-47-06_False_0.csv, day_log_12-02_21-47-06_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_21-48-06_False_0.csv, day_log_12-02_21-48-06_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-48-22_True_5.csv, day_log_12-02_21-48-22_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 5 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_21-49-03_True_0.csv, day_log_12-02_21-49-03_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_21-55-11_False_0.csv, day_log_12-02_21-55-11_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_21-56-04_True_0.csv, day_log_12-02_21-56-04_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_21-57-00_True_0.csv, day_log_12-02_21-57-00_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_21-58-31_True_10.csv, day_log_12-02_21-58-31_True_10.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 10 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_21-58-59_True_0.csv, day_log_12-02_21-58-59_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_22-05-13_False_0.csv, day_log_12-02_22-05-13_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_22-06-40_False_0.csv, day_log_12-02_22-06-40_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_22-07-06_False_0.csv, day_log_12-02_22-07-06_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_22-08-33_True_50.csv, day_log_12-02_22-08-33_True_50.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 50 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_22-08-59_True_0.csv, day_log_12-02_22-08-59_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_3', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_3

day_test_log_full_12-02_22-14-55_False_0.csv, day_log_12-02_22-14-55_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_22-15-41_True_0.csv, day_log_12-02_22-15-41_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_22-16-08_True_0.csv, day_log_12-02_22-16-08_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_22-18-52_True_100.csv, day_log_12-02_22-18-52_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 100 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_22-19-03_True_0.csv, day_log_12-02_22-19-03_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_22-24-50_False_0.csv, day_log_12-02_22-24-50_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_22-26-16_False_0.csv, day_log_12-02_22-26-16_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_22-26-37_False_0.csv, day_log_12-02_22-26-37_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_22-29-08_True_0.csv, day_log_12-02_22-29-08_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_22-29-27_True_1.csv, day_log_12-02_22-29-27_True_1.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 1 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_22-34-36_False_0.csv, day_log_12-02_22-34-36_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_22-35-20_True_0.csv, day_log_12-02_22-35-20_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_22-35-39_True_0.csv, day_log_12-02_22-35-39_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_22-39-16_True_0.csv, day_log_12-02_22-39-16_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_22-39-46_True_0.csv, day_log_12-02_22-39-46_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 0 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_22-44-36_False_0.csv, day_log_12-02_22-44-36_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_22-45-45_False_0.csv, day_log_12-02_22-45-45_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_22-46-08_False_0.csv, day_log_12-02_22-46-08_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_22-49-23_True_0.csv, day_log_12-02_22-49-23_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_22-50-08_True_3.csv, day_log_12-02_22-50-08_True_3.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 3 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_22-53-20_False_0.csv, day_log_12-02_22-53-20_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_22-54-47_True_0.csv, day_log_12-02_22-54-47_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_22-55-05_True_0.csv, day_log_12-02_22-55-05_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_22-59-38_True_0.csv, day_log_12-02_22-59-38_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_23-00-33_True_5.csv, day_log_12-02_23-00-33_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 5 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_23-02-51_False_0.csv, day_log_12-02_23-02-51_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='more_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir more_layers --num_layers 4

day_test_log_full_12-02_23-05-27_False_0.csv, day_log_12-02_23-05-27_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_23-05-28_False_0.csv, day_log_12-02_23-05-28_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_23-10-03_True_0.csv, day_log_12-02_23-10-03_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_23-10-59_True_10.csv, day_log_12-02_23-10-59_True_10.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=10, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 10 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_23-13-33_True_0.csv, day_log_12-02_23-13-33_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_23-14-27_True_0.csv, day_log_12-02_23-14-27_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_23-20-20_True_0.csv, day_log_12-02_23-20-20_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_23-21-02_True_50.csv, day_log_12-02_23-21-02_True_50.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=50, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 50 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_23-23-36_False_0.csv, day_log_12-02_23-23-36_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_23-24-37_False_0.csv, day_log_12-02_23-24-37_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_23-30-33_True_0.csv, day_log_12-02_23-30-33_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_23-31-04_True_100.csv, day_log_12-02_23-31-04_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='grid_search_ae_resample_.645', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 100 --log_subdir grid_search_ae_resample_.645

day_test_log_full_12-02_23-32-20_True_0.csv, day_log_12-02_23-32-20_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_23-33-26_True_0.csv, day_log_12-02_23-33-26_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_23-39-41_True_0.csv, day_log_12-02_23-39-41_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_4', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_4

day_test_log_full_12-02_23-42-14_False_0.csv, day_log_12-02_23-42-14_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-02_23-43-24_False_0.csv, day_log_12-02_23-43-24_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_23-49-14_True_0.csv, day_log_12-02_23-49-14_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-02_23-51-16_True_0.csv, day_log_12-02_23-51-16_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-02_23-52-25_True_0.csv, day_log_12-02_23-52-25_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-02_23-59-04_True_0.csv, day_log_12-02_23-59-04_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_00-01-19_False_0.csv, day_log_12-03_00-01-19_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --log_subdir repeats_.645

day_test_log_full_12-03_00-02-28_False_0.csv, day_log_12-03_00-02-28_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-03_00-08-25_True_0.csv, day_log_12-03_00-08-25_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_00-09-38_True_0.csv, day_log_12-03_00-09-38_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.645', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --log_subdir repeats_.645

day_test_log_full_12-03_00-09-50_True_0.csv, day_log_12-03_00-09-50_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-03_00-16-29_True_0.csv, day_log_12-03_00-16-29_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_00-19-05_False_0.csv, day_log_12-03_00-19-05_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-03_00-25-34_True_0.csv, day_log_12-03_00-25-34_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_00-27-54_True_0.csv, day_log_12-03_00-27-54_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-03_00-34-53_True_0.csv, day_log_12-03_00-34-53_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_00-37-30_False_0.csv, day_log_12-03_00-37-30_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0 --normalize --log_subdir repeats_.05

day_test_log_full_12-03_00-44-18_True_0.csv, day_log_12-03_00-44-18_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_00-46-24_True_0.csv, day_log_12-03_00-46-24_True_0.csv
Namespace(ae=0.05, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='repeats_.05', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.05 --normalize --log_subdir repeats_.05

day_test_log_full_12-03_00-53-45_True_0.csv, day_log_12-03_00-53-45_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_01-03-03_True_0.csv, day_log_12-03_01-03-03_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_5', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_5

day_test_log_full_12-03_01-12-34_True_0.csv, day_log_12-03_01-12-34_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_01-22-01_True_0.csv, day_log_12-03_01-22-01_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_01-31-27_True_0.csv, day_log_12-03_01-31-27_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_01-40-55_True_0.csv, day_log_12-03_01-40-55_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_01-50-29_True_0.csv, day_log_12-03_01-50-29_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_01-59-59_True_0.csv, day_log_12-03_01-59-59_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_02-09-26_True_0.csv, day_log_12-03_02-09-26_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_02-18-55_True_0.csv, day_log_12-03_02-18-55_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_02-28-25_True_0.csv, day_log_12-03_02-28-25_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_6', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_6

day_test_log_full_12-03_02-37-58_True_0.csv, day_log_12-03_02-37-58_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_02-47-24_True_0.csv, day_log_12-03_02-47-24_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_02-56-51_True_0.csv, day_log_12-03_02-56-51_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_03-06-25_True_0.csv, day_log_12-03_03-06-25_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_03-15-54_True_0.csv, day_log_12-03_03-15-54_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_03-25-23_True_0.csv, day_log_12-03_03-25-23_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_03-34-56_True_0.csv, day_log_12-03_03-34-56_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_03-44-38_True_0.csv, day_log_12-03_03-44-38_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_03-54-10_True_0.csv, day_log_12-03_03-54-10_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_7', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_7

day_test_log_full_12-03_04-03-40_True_0.csv, day_log_12-03_04-03-40_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_04-13-11_True_0.csv, day_log_12-03_04-13-11_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_04-22-35_True_0.csv, day_log_12-03_04-22-35_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_04-32-08_True_0.csv, day_log_12-03_04-32-08_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_04-41-41_True_0.csv, day_log_12-03_04-41-41_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_04-51-06_True_0.csv, day_log_12-03_04-51-06_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_05-00-33_True_0.csv, day_log_12-03_05-00-33_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_05-10-00_True_0.csv, day_log_12-03_05-10-00_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_05-19-33_True_0.csv, day_log_12-03_05-19-33_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_8', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_8

day_test_log_full_12-03_05-29-29_True_0.csv, day_log_12-03_05-29-29_True_0.csv
Namespace(ae=0.58, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.58 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_05-39-25_True_0.csv, day_log_12-03_05-39-25_True_0.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.60 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_05-49-00_True_0.csv, day_log_12-03_05-49-00_True_0.csv
Namespace(ae=0.62, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.62 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_05-58-55_True_0.csv, day_log_12-03_05-58-55_True_0.csv
Namespace(ae=0.64, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.64 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_06-08-28_True_0.csv, day_log_12-03_06-08-28_True_0.csv
Namespace(ae=0.66, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.66 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_06-18-08_True_0.csv, day_log_12-03_06-18-08_True_0.csv
Namespace(ae=0.68, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.68 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_06-27-40_True_0.csv, day_log_12-03_06-27-40_True_0.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.70 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_06-37-09_True_0.csv, day_log_12-03_06-37-09_True_0.csv
Namespace(ae=0.72, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.72 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_06-46-32_True_0.csv, day_log_12-03_06-46-32_True_0.csv
Namespace(ae=0.74, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='gird_search_ae_repeats/0.58_9', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.74 --normalize --log_subdir gird_search_ae_repeats/0.58_9

day_test_log_full_12-03_23-25-00_False_5.csv, day_log_12-03_23-25-00_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-03_23-33-16_True_5.csv, day_log_12-03_23-33-16_True_5.csv
Namespace(ae=0.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-03_23-42-25_True_5.csv, day_log_12-03_23-42-25_True_5.csv
Namespace(ae=0.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-03_23-51-28_True_5.csv, day_log_12-03_23-51-28_True_5.csv
Namespace(ae=0.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-00-30_True_5.csv, day_log_12-04_00-00-30_True_5.csv
Namespace(ae=0.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-09-30_True_5.csv, day_log_12-04_00-09-30_True_5.csv
Namespace(ae=0.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-18-28_True_5.csv, day_log_12-04_00-18-28_True_5.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-27-30_True_5.csv, day_log_12-04_00-27-30_True_5.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-36-25_True_5.csv, day_log_12-04_00-36-25_True_5.csv
Namespace(ae=0.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-45-25_True_5.csv, day_log_12-04_00-45-25_True_5.csv
Namespace(ae=0.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_00-54-22_True_5.csv, day_log_12-04_00-54-22_True_5.csv
Namespace(ae=1.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-03-26_True_5.csv, day_log_12-04_01-03-26_True_5.csv
Namespace(ae=1.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-12-30_True_5.csv, day_log_12-04_01-12-30_True_5.csv
Namespace(ae=1.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-21-32_True_5.csv, day_log_12-04_01-21-32_True_5.csv
Namespace(ae=1.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-30-32_True_5.csv, day_log_12-04_01-30-32_True_5.csv
Namespace(ae=1.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-39-33_True_5.csv, day_log_12-04_01-39-33_True_5.csv
Namespace(ae=1.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-48-27_True_5.csv, day_log_12-04_01-48-27_True_5.csv
Namespace(ae=1.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_01-57-28_True_5.csv, day_log_12-04_01-57-28_True_5.csv
Namespace(ae=1.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_02-06-27_True_5.csv, day_log_12-04_02-06-27_True_5.csv
Namespace(ae=1.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_02-15-26_True_5.csv, day_log_12-04_02-15-26_True_5.csv
Namespace(ae=1.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_02-24-23_True_5.csv, day_log_12-04_02-24-23_True_5.csv
Namespace(ae=2.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_02-33-23_True_5.csv, day_log_12-04_02-33-23_True_5.csv
Namespace(ae=2.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_02-42-23_True_5.csv, day_log_12-04_02-42-23_True_5.csv
Namespace(ae=2.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_02-51-25_True_5.csv, day_log_12-04_02-51-25_True_5.csv
Namespace(ae=2.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-00-22_True_5.csv, day_log_12-04_03-00-22_True_5.csv
Namespace(ae=2.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-09-29_True_5.csv, day_log_12-04_03-09-29_True_5.csv
Namespace(ae=2.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-18-31_True_5.csv, day_log_12-04_03-18-31_True_5.csv
Namespace(ae=2.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-27-35_True_5.csv, day_log_12-04_03-27-35_True_5.csv
Namespace(ae=2.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-36-35_True_5.csv, day_log_12-04_03-36-35_True_5.csv
Namespace(ae=2.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-45-35_True_5.csv, day_log_12-04_03-45-35_True_5.csv
Namespace(ae=2.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_03-54-39_True_5.csv, day_log_12-04_03-54-39_True_5.csv
Namespace(ae=3.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-03-43_True_5.csv, day_log_12-04_04-03-43_True_5.csv
Namespace(ae=3.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-12-41_True_5.csv, day_log_12-04_04-12-41_True_5.csv
Namespace(ae=3.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-21-49_True_5.csv, day_log_12-04_04-21-49_True_5.csv
Namespace(ae=3.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-30-56_True_5.csv, day_log_12-04_04-30-56_True_5.csv
Namespace(ae=3.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-39-58_True_5.csv, day_log_12-04_04-39-58_True_5.csv
Namespace(ae=3.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-48-58_True_5.csv, day_log_12-04_04-48-58_True_5.csv
Namespace(ae=3.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_04-58-04_True_5.csv, day_log_12-04_04-58-04_True_5.csv
Namespace(ae=3.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_05-07-16_True_5.csv, day_log_12-04_05-07-16_True_5.csv
Namespace(ae=3.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_05-16-26_True_5.csv, day_log_12-04_05-16-26_True_5.csv
Namespace(ae=3.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 3.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_05-25-30_True_5.csv, day_log_12-04_05-25-30_True_5.csv
Namespace(ae=4.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_05-34-39_True_5.csv, day_log_12-04_05-34-39_True_5.csv
Namespace(ae=4.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_05-43-36_True_5.csv, day_log_12-04_05-43-36_True_5.csv
Namespace(ae=4.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_05-52-35_True_5.csv, day_log_12-04_05-52-35_True_5.csv
Namespace(ae=4.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-01-38_True_5.csv, day_log_12-04_06-01-38_True_5.csv
Namespace(ae=4.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-10-43_True_5.csv, day_log_12-04_06-10-43_True_5.csv
Namespace(ae=4.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-19-54_True_5.csv, day_log_12-04_06-19-54_True_5.csv
Namespace(ae=4.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-29-09_True_5.csv, day_log_12-04_06-29-09_True_5.csv
Namespace(ae=4.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-38-25_True_5.csv, day_log_12-04_06-38-25_True_5.csv
Namespace(ae=4.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-47-38_True_5.csv, day_log_12-04_06-47-38_True_5.csv
Namespace(ae=4.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 4.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_06-56-53_True_5.csv, day_log_12-04_06-56-53_True_5.csv
Namespace(ae=5.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/1', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 5.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/1

day_test_log_full_12-04_07-06-08_False_5.csv, day_log_12-04_07-06-08_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_07-14-44_True_5.csv, day_log_12-04_07-14-44_True_5.csv
Namespace(ae=0.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_07-24-01_True_5.csv, day_log_12-04_07-24-01_True_5.csv
Namespace(ae=0.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_07-33-14_True_5.csv, day_log_12-04_07-33-14_True_5.csv
Namespace(ae=0.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_07-42-24_True_5.csv, day_log_12-04_07-42-24_True_5.csv
Namespace(ae=0.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_07-51-36_True_5.csv, day_log_12-04_07-51-36_True_5.csv
Namespace(ae=0.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-00-47_True_5.csv, day_log_12-04_08-00-47_True_5.csv
Namespace(ae=0.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-10-00_True_5.csv, day_log_12-04_08-10-00_True_5.csv
Namespace(ae=0.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-19-20_True_5.csv, day_log_12-04_08-19-20_True_5.csv
Namespace(ae=0.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-28-39_True_5.csv, day_log_12-04_08-28-39_True_5.csv
Namespace(ae=0.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-37-50_True_5.csv, day_log_12-04_08-37-50_True_5.csv
Namespace(ae=1.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-47-07_True_5.csv, day_log_12-04_08-47-07_True_5.csv
Namespace(ae=1.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_08-56-22_True_5.csv, day_log_12-04_08-56-22_True_5.csv
Namespace(ae=1.2, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.2 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_09-05-38_True_5.csv, day_log_12-04_09-05-38_True_5.csv
Namespace(ae=1.3, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.3 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_09-14-51_True_5.csv, day_log_12-04_09-14-51_True_5.csv
Namespace(ae=1.4, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.4 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_09-24-04_True_5.csv, day_log_12-04_09-24-04_True_5.csv
Namespace(ae=1.5, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.5 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_09-33-20_True_5.csv, day_log_12-04_09-33-20_True_5.csv
Namespace(ae=1.6, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.6 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_09-42-39_True_5.csv, day_log_12-04_09-42-39_True_5.csv
Namespace(ae=1.7, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.7 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_09-51-57_True_5.csv, day_log_12-04_09-51-57_True_5.csv
Namespace(ae=1.8, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.8 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_10-01-18_True_5.csv, day_log_12-04_10-01-18_True_5.csv
Namespace(ae=1.9, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 1.9 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_10-10-23_True_5.csv, day_log_12-04_10-10-23_True_5.csv
Namespace(ae=2.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.0 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_10-19-42_True_5.csv, day_log_12-04_10-19-42_True_5.csv
Namespace(ae=2.1, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='5_samples_repeats_.05/2', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 2.1 --num_day_resample 5 --log_subdir 5_samples_repeats_.05/2

day_test_log_full_12-04_21-24-35_False_0.csv, day_log_12-04_21-24-35_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-04_21-32-28_False_5.csv, day_log_12-04_21-32-28_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-04_21-33-22_False_0.csv, day_log_12-04_21-33-22_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result --test

day_test_log_full_12-04_21-40-37_False_100.csv, day_log_12-04_21-40-37_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-04_21-47-22_False_5.csv, day_log_12-04_21-47-22_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result --test

day_test_log_full_12-04_21-48-57_True_0.csv, day_log_12-04_21-48-57_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-04_21-56-54_True_5.csv, day_log_12-04_21-56-54_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 5 --log_subdir test_result --test

day_test_log_full_12-04_21-57-04_True_5.csv, day_log_12-04_21-57-04_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-04_22-06-02_True_100.csv, day_log_12-04_22-06-02_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-04_22-14-24_True_0.csv, day_log_12-04_22-14-24_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae .645 --num_day_resample 0 --log_subdir test_result --test

day_test_log_full_12-04_22-15-09_False_0.csv, day_log_12-04_22-15-09_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-04_22-23-32_False_5.csv, day_log_12-04_22-23-32_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-04_22-28-58_False_0.csv, day_log_12-04_22-28-58_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.1, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --cw .1 --num_day_resample 0 --log_subdir test_result --test

day_test_log_full_12-04_22-29-54_False_0.csv, day_log_12-04_22-29-54_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.1, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --cw_weight .1 --num_day_resample 0 --log_subdir test_result --test

day_test_log_full_12-04_22-32-04_False_100.csv, day_log_12-04_22-32-04_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-04_22-39-54_False_5.csv, day_log_12-04_22-39-54_False_5.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0.1, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --cw_weight .1 --num_day_resample 5 --log_subdir test_result --test

day_test_log_full_12-04_22-40-38_True_0.csv, day_log_12-04_22-40-38_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-04_22-49-50_True_5.csv, day_log_12-04_22-49-50_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-04_22-58-14_True_100.csv, day_log_12-04_22-58-14_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-04_23-01-30.csv, log_12-04_23-01-30.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=0, epochs=10, epochs_warm=5, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=180)
main.py --cuda --epochs 10 --normalize --log_subdir test_result --test

day_test_log_full_12-04_23-07-29_False_0.csv, day_log_12-04_23-07-29_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-04_23-16-02_False_5.csv, day_log_12-04_23-16-02_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-04_23-24-36_False_100.csv, day_log_12-04_23-24-36_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-04_23-32-12_True_0.csv, day_log_12-04_23-32-12_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-04_23-40-15.csv, log_12-04_23-40-15.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=10, epochs_warm=5, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=180)
main.py --cuda --epochs 10 --normalize --log_subdir test_result --test --epoch_days_test 10

day_test_log_full_12-04_23-41-20_True_5.csv, day_log_12-04_23-41-20_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-04_23-50-31_True_100.csv, day_log_12-04_23-50-31_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-04_23-59-05_False_0.csv, day_log_12-04_23-59-05_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_00-07-43_False_5.csv, day_log_12-05_00-07-43_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_00-13-30.csv, log_12-05_00-13-30.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=10, epochs_warm=5, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=180)
main.py --cuda --epochs 10 --normalize --log_subdir test_result --test --epoch_days_test 10

day_test_log_full_12-05_00-16-18_False_100.csv, day_log_12-05_00-16-18_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_00-23-46_True_0.csv, day_log_12-05_00-23-46_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_00-32-57_True_5.csv, day_log_12-05_00-32-57_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_00-42-15_True_100.csv, day_log_12-05_00-42-15_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_00-51-41_False_0.csv, day_log_12-05_00-51-41_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_01-00-45_False_5.csv, day_log_12-05_01-00-45_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_01-09-15_False_100.csv, day_log_12-05_01-09-15_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_01-18-02_True_0.csv, day_log_12-05_01-18-02_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_01-24-11_False_0.csv, day_log_12-05_01-24-11_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_01-24-43_False_0.csv, day_log_12-05_01-24-43_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_01-27-30_True_5.csv, day_log_12-05_01-27-30_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_01-31-35_False_5.csv, day_log_12-05_01-31-35_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_01-31-36_False_5.csv, day_log_12-05_01-31-36_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_01-36-15_True_100.csv, day_log_12-05_01-36-15_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_01-39-39_False_100.csv, day_log_12-05_01-39-39_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_01-39-50_False_100.csv, day_log_12-05_01-39-50_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_01-45-28_False_0.csv, day_log_12-05_01-45-28_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_01-47-09_True_0.csv, day_log_12-05_01-47-09_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_01-47-11_True_0.csv, day_log_12-05_01-47-11_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_01-54-09_False_5.csv, day_log_12-05_01-54-09_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_01-55-39_True_5.csv, day_log_12-05_01-55-39_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_01-55-58_True_5.csv, day_log_12-05_01-55-58_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_02-02-42_False_100.csv, day_log_12-05_02-02-42_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_02-04-39_True_100.csv, day_log_12-05_02-04-39_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_02-05-06_True_100.csv, day_log_12-05_02-05-06_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_02-11-25_True_0.csv, day_log_12-05_02-11-25_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_02-13-36_False_0.csv, day_log_12-05_02-13-36_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_02-14-16_False_0.csv, day_log_12-05_02-14-16_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_02-21-16_True_5.csv, day_log_12-05_02-21-16_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_02-21-27_False_5.csv, day_log_12-05_02-21-27_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_02-22-42_False_5.csv, day_log_12-05_02-22-42_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_02-30-08_False_100.csv, day_log_12-05_02-30-08_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_02-31-07_True_100.csv, day_log_12-05_02-31-07_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_02-31-22_False_100.csv, day_log_12-05_02-31-22_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_02-38-53_True_0.csv, day_log_12-05_02-38-53_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_02-40-10_True_0.csv, day_log_12-05_02-40-10_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_02-40-58_False_0.csv, day_log_12-05_02-40-58_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_02-48-26_True_5.csv, day_log_12-05_02-48-26_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_02-49-43_True_5.csv, day_log_12-05_02-49-43_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_02-49-51_False_5.csv, day_log_12-05_02-49-51_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_02-57-31_True_100.csv, day_log_12-05_02-57-31_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_02-58-08_True_100.csv, day_log_12-05_02-58-08_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_02-58-32_False_100.csv, day_log_12-05_02-58-32_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_03-06-51_False_0.csv, day_log_12-05_03-06-51_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_03-07-31_False_0.csv, day_log_12-05_03-07-31_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_03-07-52_True_0.csv, day_log_12-05_03-07-52_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_03-15-34_False_5.csv, day_log_12-05_03-15-34_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_03-15-49_False_5.csv, day_log_12-05_03-15-49_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_03-17-11_True_5.csv, day_log_12-05_03-17-11_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_03-24-05_False_100.csv, day_log_12-05_03-24-05_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_03-24-07_False_100.csv, day_log_12-05_03-24-07_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_03-26-11_True_100.csv, day_log_12-05_03-26-11_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_03-32-49_True_0.csv, day_log_12-05_03-32-49_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_03-32-49_True_0.csv, day_log_12-05_03-32-49_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_03-35-08_False_0.csv, day_log_12-05_03-35-08_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_03-42-34_True_5.csv, day_log_12-05_03-42-34_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_03-42-37_True_5.csv, day_log_12-05_03-42-37_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_03-43-28_False_5.csv, day_log_12-05_03-43-28_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_03-51-44_False_100.csv, day_log_12-05_03-51-44_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_03-52-10_True_100.csv, day_log_12-05_03-52-10_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_03-52-17_True_100.csv, day_log_12-05_03-52-17_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_04-00-15_True_0.csv, day_log_12-05_04-00-15_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_04-01-25_False_0.csv, day_log_12-05_04-01-25_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_04-02-08_False_0.csv, day_log_12-05_04-02-08_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_04-09-32_True_5.csv, day_log_12-05_04-09-32_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_04-09-33_False_5.csv, day_log_12-05_04-09-33_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_04-10-50_False_5.csv, day_log_12-05_04-10-50_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_04-17-53_False_100.csv, day_log_12-05_04-17-53_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_04-18-11_False_100.csv, day_log_12-05_04-18-11_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_04-18-55_True_100.csv, day_log_12-05_04-18-55_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_04-26-19_True_0.csv, day_log_12-05_04-26-19_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_04-26-40_True_0.csv, day_log_12-05_04-26-40_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_04-29-10_False_0.csv, day_log_12-05_04-29-10_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_04-35-29_True_5.csv, day_log_12-05_04-35-29_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_04-35-51_True_5.csv, day_log_12-05_04-35-51_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_04-37-56_False_5.csv, day_log_12-05_04-37-56_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_04-44-20_True_100.csv, day_log_12-05_04-44-20_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_04-44-55_True_100.csv, day_log_12-05_04-44-55_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_04-45-12_False_100.csv, day_log_12-05_04-45-12_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_04-52-59_True_0.csv, day_log_12-05_04-52-59_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_04-54-08_False_0.csv, day_log_12-05_04-54-08_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_04-54-24_False_0.csv, day_log_12-05_04-54-24_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_05-02-01_True_5.csv, day_log_12-05_05-02-01_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_05-02-47_False_5.csv, day_log_12-05_05-02-47_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_05-02-54_False_5.csv, day_log_12-05_05-02-54_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_05-11-21_False_100.csv, day_log_12-05_05-11-21_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_05-11-22_True_100.csv, day_log_12-05_05-11-22_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_05-11-36_False_100.csv, day_log_12-05_05-11-36_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_05-18-56_True_0.csv, day_log_12-05_05-18-56_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_05-19-54_True_0.csv, day_log_12-05_05-19-54_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_05-20-41_False_0.csv, day_log_12-05_05-20-41_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_05-28-29_True_5.csv, day_log_12-05_05-28-29_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_05-28-36_False_5.csv, day_log_12-05_05-28-36_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_05-29-40_True_5.csv, day_log_12-05_05-29-40_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_05-36-48_False_100.csv, day_log_12-05_05-36-48_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_05-37-52_True_100.csv, day_log_12-05_05-37-52_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_05-38-27_True_100.csv, day_log_12-05_05-38-27_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_05-45-32_True_0.csv, day_log_12-05_05-45-32_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_05-47-33_False_0.csv, day_log_12-05_05-47-33_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_05-47-44_False_0.csv, day_log_12-05_05-47-44_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_05-55-02_True_5.csv, day_log_12-05_05-55-02_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_05-56-04_False_5.csv, day_log_12-05_05-56-04_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_05-56-18_False_5.csv, day_log_12-05_05-56-18_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_06-04-43_False_100.csv, day_log_12-05_06-04-43_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_06-04-59_True_100.csv, day_log_12-05_06-04-59_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_06-04-59_False_100.csv, day_log_12-05_06-04-59_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_06-13-14_True_0.csv, day_log_12-05_06-13-14_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_06-13-15_True_0.csv, day_log_12-05_06-13-15_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_06-14-43_False_0.csv, day_log_12-05_06-14-43_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_06-22-43_True_5.csv, day_log_12-05_06-22-43_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_06-22-46_True_5.csv, day_log_12-05_06-22-46_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_06-23-35_False_5.csv, day_log_12-05_06-23-35_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_06-32-12_True_100.csv, day_log_12-05_06-32-12_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_06-32-17_True_100.csv, day_log_12-05_06-32-17_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_06-32-23_False_100.csv, day_log_12-05_06-32-23_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_06-40-36_True_0.csv, day_log_12-05_06-40-36_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_06-42-01_False_0.csv, day_log_12-05_06-42-01_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_06-42-07_False_0.csv, day_log_12-05_06-42-07_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_06-50-06_True_5.csv, day_log_12-05_06-50-06_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_06-50-42_False_5.csv, day_log_12-05_06-50-42_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_06-50-49_False_5.csv, day_log_12-05_06-50-49_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_06-59-04_False_100.csv, day_log_12-05_06-59-04_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_06-59-22_True_100.csv, day_log_12-05_06-59-22_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_06-59-26_False_100.csv, day_log_12-05_06-59-26_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_07-07-22_True_0.csv, day_log_12-05_07-07-22_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_07-07-41_True_0.csv, day_log_12-05_07-07-41_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_07-09-11_False_0.csv, day_log_12-05_07-09-11_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_07-16-57_True_5.csv, day_log_12-05_07-16-57_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_07-17-04_True_5.csv, day_log_12-05_07-17-04_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_07-17-54_False_5.csv, day_log_12-05_07-17-54_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_07-25-25_False_100.csv, day_log_12-05_07-25-25_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_07-26-19_True_100.csv, day_log_12-05_07-26-19_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_07-26-20_True_100.csv, day_log_12-05_07-26-20_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_07-33-04_True_0.csv, day_log_12-05_07-33-04_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_07-35-39_False_0.csv, day_log_12-05_07-35-39_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_07-35-57_False_0.csv, day_log_12-05_07-35-57_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_07-42-07_True_5.csv, day_log_12-05_07-42-07_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_07-43-07_False_5.csv, day_log_12-05_07-43-07_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_07-44-10_False_5.csv, day_log_12-05_07-44-10_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_07-51-24_False_100.csv, day_log_12-05_07-51-24_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_07-51-47_True_100.csv, day_log_12-05_07-51-47_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_07-51-55_False_100.csv, day_log_12-05_07-51-55_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_07-59-53_True_0.csv, day_log_12-05_07-59-53_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_08-00-10_True_0.csv, day_log_12-05_08-00-10_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_08-01-36_False_0.csv, day_log_12-05_08-01-36_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_08-09-12_True_5.csv, day_log_12-05_08-09-12_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_08-09-22_True_5.csv, day_log_12-05_08-09-22_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_08-10-21_False_5.csv, day_log_12-05_08-10-21_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_08-18-40_True_100.csv, day_log_12-05_08-18-40_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_08-18-46_True_100.csv, day_log_12-05_08-18-46_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_08-19-14_False_100.csv, day_log_12-05_08-19-14_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_08-27-33_False_0.csv, day_log_12-05_08-27-33_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_08-27-37_True_0.csv, day_log_12-05_08-27-37_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_08-27-59_False_0.csv, day_log_12-05_08-27-59_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_08-35-56_False_5.csv, day_log_12-05_08-35-56_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_08-36-15_False_5.csv, day_log_12-05_08-36-15_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_08-37-10_True_5.csv, day_log_12-05_08-37-10_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_08-44-08_False_100.csv, day_log_12-05_08-44-08_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_08-44-36_False_100.csv, day_log_12-05_08-44-36_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_08-46-33_True_100.csv, day_log_12-05_08-46-33_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_08-52-11_True_0.csv, day_log_12-05_08-52-11_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_08-52-42_True_0.csv, day_log_12-05_08-52-42_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_08-55-59_False_0.csv, day_log_12-05_08-55-59_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_09-01-23_True_5.csv, day_log_12-05_09-01-23_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_09-02-11_True_5.csv, day_log_12-05_09-02-11_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_09-04-36_False_5.csv, day_log_12-05_09-04-36_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_09-10-33_True_100.csv, day_log_12-05_09-10-33_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_09-11-53_True_100.csv, day_log_12-05_09-11-53_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_09-13-22_False_100.csv, day_log_12-05_09-13-22_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_09-20-00_False_0.csv, day_log_12-05_09-20-00_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_09-21-43_False_0.csv, day_log_12-05_09-21-43_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_09-22-16_True_0.csv, day_log_12-05_09-22-16_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_09-28-32_False_5.csv, day_log_12-05_09-28-32_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_09-30-36_False_5.csv, day_log_12-05_09-30-36_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_09-32-06_True_5.csv, day_log_12-05_09-32-06_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_09-37-08_False_100.csv, day_log_12-05_09-37-08_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_09-39-26_False_100.csv, day_log_12-05_09-39-26_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_09-41-47_True_100.csv, day_log_12-05_09-41-47_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_09-45-37_True_0.csv, day_log_12-05_09-45-37_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_09-47-44_True_0.csv, day_log_12-05_09-47-44_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_09-50-18_False_0.csv, day_log_12-05_09-50-18_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_09-53-51_True_5.csv, day_log_12-05_09-53-51_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_09-57-04_True_5.csv, day_log_12-05_09-57-04_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_09-58-53_False_5.csv, day_log_12-05_09-58-53_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_10-03-11_True_100.csv, day_log_12-05_10-03-11_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_10-06-02_True_100.csv, day_log_12-05_10-06-02_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_10-07-36_False_100.csv, day_log_12-05_10-07-36_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_10-12-17_False_0.csv, day_log_12-05_10-12-17_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_10-15-31_False_0.csv, day_log_12-05_10-15-31_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_10-16-26_True_0.csv, day_log_12-05_10-16-26_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_10-20-50_False_5.csv, day_log_12-05_10-20-50_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_10-24-02_False_5.csv, day_log_12-05_10-24-02_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_10-26-09_True_5.csv, day_log_12-05_10-26-09_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_10-29-10_False_100.csv, day_log_12-05_10-29-10_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_10-32-35_False_100.csv, day_log_12-05_10-32-35_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_10-35-43_True_100.csv, day_log_12-05_10-35-43_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_10-37-40_True_0.csv, day_log_12-05_10-37-40_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_10-41-23_True_0.csv, day_log_12-05_10-41-23_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_10-45-34_False_0.csv, day_log_12-05_10-45-34_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_10-46-57_True_5.csv, day_log_12-05_10-46-57_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_10-50-43_True_5.csv, day_log_12-05_10-50-43_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_10-54-16_False_5.csv, day_log_12-05_10-54-16_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_10-56-18_True_100.csv, day_log_12-05_10-56-18_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_10-59-58_True_100.csv, day_log_12-05_10-59-58_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_11-02-58_False_100.csv, day_log_12-05_11-02-58_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_11-05-53_False_0.csv, day_log_12-05_11-05-53_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_11-09-15_False_0.csv, day_log_12-05_11-09-15_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_11-11-50_True_0.csv, day_log_12-05_11-11-50_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_11-14-39_False_5.csv, day_log_12-05_11-14-39_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_11-17-38_False_5.csv, day_log_12-05_11-17-38_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_11-21-33_True_5.csv, day_log_12-05_11-21-33_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_11-23-27_False_100.csv, day_log_12-05_11-23-27_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_11-25-58_False_100.csv, day_log_12-05_11-25-58_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_11-31-16_True_100.csv, day_log_12-05_11-31-16_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_11-32-24_True_0.csv, day_log_12-05_11-32-24_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_11-34-27_True_0.csv, day_log_12-05_11-34-27_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_11-40-25_False_0.csv, day_log_12-05_11-40-25_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_11-42-00_True_5.csv, day_log_12-05_11-42-00_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_11-43-53_True_5.csv, day_log_12-05_11-43-53_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_11-48-53_False_5.csv, day_log_12-05_11-48-53_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_11-51-56_True_100.csv, day_log_12-05_11-51-56_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_11-53-29_True_100.csv, day_log_12-05_11-53-29_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_11-57-15_False_100.csv, day_log_12-05_11-57-15_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_12-01-53_False_0.csv, day_log_12-05_12-01-53_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_12-03-18_False_0.csv, day_log_12-05_12-03-18_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_12-05-46_True_0.csv, day_log_12-05_12-05-46_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_12-10-56_False_5.csv, day_log_12-05_12-10-56_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_12-12-03_False_5.csv, day_log_12-05_12-12-03_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_12-15-11_True_5.csv, day_log_12-05_12-15-11_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_12-19-54_False_100.csv, day_log_12-05_12-19-54_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_12-20-59_False_100.csv, day_log_12-05_12-20-59_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_12-24-38_True_100.csv, day_log_12-05_12-24-38_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_12-28-06_True_0.csv, day_log_12-05_12-28-06_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_12-28-30_True_0.csv, day_log_12-05_12-28-30_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_12-34-33_False_0.csv, day_log_12-05_12-34-33_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_12-37-20_True_5.csv, day_log_12-05_12-37-20_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_12-37-39_True_5.csv, day_log_12-05_12-37-39_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_12-43-22_False_5.csv, day_log_12-05_12-43-22_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_12-46-50_True_100.csv, day_log_12-05_12-46-50_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_12-46-58_True_100.csv, day_log_12-05_12-46-58_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_12-50-37_False_100.csv, day_log_12-05_12-50-37_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_12-56-20_False_0.csv, day_log_12-05_12-56-20_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_12-56-22_False_0.csv, day_log_12-05_12-56-22_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_12-59-07_True_0.csv, day_log_12-05_12-59-07_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_13-04-43_False_5.csv, day_log_12-05_13-04-43_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_13-04-57_False_5.csv, day_log_12-05_13-04-57_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_13-07-39_True_5.csv, day_log_12-05_13-07-39_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_13-12-51_False_100.csv, day_log_12-05_13-12-51_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_13-13-10_False_100.csv, day_log_12-05_13-13-10_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_13-16-59_True_100.csv, day_log_12-05_13-16-59_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_13-21-12_True_0.csv, day_log_12-05_13-21-12_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_13-21-40_True_0.csv, day_log_12-05_13-21-40_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_13-25-32_False_0.csv, day_log_12-05_13-25-32_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_13-30-39_True_5.csv, day_log_12-05_13-30-39_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_13-30-42_True_5.csv, day_log_12-05_13-30-42_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_13-33-57_False_5.csv, day_log_12-05_13-33-57_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_13-40-06_True_100.csv, day_log_12-05_13-40-06_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_13-40-21_True_100.csv, day_log_12-05_13-40-21_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_13-41-25_False_100.csv, day_log_12-05_13-41-25_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_13-49-11_True_0.csv, day_log_12-05_13-49-11_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_13-49-40_False_0.csv, day_log_12-05_13-49-40_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_13-50-20_False_0.csv, day_log_12-05_13-50-20_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_13-58-22_False_5.csv, day_log_12-05_13-58-22_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_13-58-25_True_5.csv, day_log_12-05_13-58-25_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_13-59-04_False_5.csv, day_log_12-05_13-59-04_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_14-06-58_False_100.csv, day_log_12-05_14-06-58_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_14-07-39_True_100.csv, day_log_12-05_14-07-39_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_14-07-48_False_100.csv, day_log_12-05_14-07-48_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_14-16-03_True_0.csv, day_log_12-05_14-16-03_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_14-16-27_True_0.csv, day_log_12-05_14-16-27_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_14-17-36_False_0.csv, day_log_12-05_14-17-36_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_14-25-55_True_5.csv, day_log_12-05_14-25-55_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_14-25-57_True_5.csv, day_log_12-05_14-25-57_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_14-26-26_False_5.csv, day_log_12-05_14-26-26_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_14-34-43_False_100.csv, day_log_12-05_14-34-43_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_14-35-26_True_100.csv, day_log_12-05_14-35-26_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_14-35-28_True_100.csv, day_log_12-05_14-35-28_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_14-43-38_True_0.csv, day_log_12-05_14-43-38_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0 --test

day_test_log_full_12-05_14-45-13_False_0.csv, day_log_12-05_14-45-13_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_14-45-20_False_0.csv, day_log_12-05_14-45-20_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_14-53-24_True_5.csv, day_log_12-05_14-53-24_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5 --test

day_test_log_full_12-05_14-53-38_False_5.csv, day_log_12-05_14-53-38_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_14-53-55_False_5.csv, day_log_12-05_14-53-55_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_15-02-05_False_100.csv, day_log_12-05_15-02-05_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_15-03-08_False_100.csv, day_log_12-05_15-03-08_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_15-03-23_True_100.csv, day_log_12-05_15-03-23_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100 --test

day_test_log_full_12-05_15-10-43_True_0.csv, day_log_12-05_15-10-43_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_15-11-59_True_0.csv, day_log_12-05_15-11-59_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_15-20-12_True_5.csv, day_log_12-05_15-20-12_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_15-21-34_True_5.csv, day_log_12-05_15-21-34_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_15-29-31_True_100.csv, day_log_12-05_15-29-31_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_15-30-11_True_100.csv, day_log_12-05_15-30-11_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_15-38-54_False_0.csv, day_log_12-05_15-38-54_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_15-39-08_False_0.csv, day_log_12-05_15-39-08_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_15-47-32_False_5.csv, day_log_12-05_15-47-32_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_15-47-33_False_5.csv, day_log_12-05_15-47-33_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_15-56-03_False_100.csv, day_log_12-05_15-56-03_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_15-56-20_False_100.csv, day_log_12-05_15-56-20_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_16-03-16_False_0.csv, day_log_12-05_16-03-16_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-04-24_True_0.csv, day_log_12-05_16-04-24_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_16-04-56_True_0.csv, day_log_12-05_16-04-56_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_16-11-54_False_0.csv, day_log_12-05_16-11-54_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-12-30_True_5.csv, day_log_12-05_16-12-30_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_16-14-39_True_5.csv, day_log_12-05_16-14-39_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_16-21-17_False_0.csv, day_log_12-05_16-21-17_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-21-40_True_100.csv, day_log_12-05_16-21-40_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_16-23-43_True_100.csv, day_log_12-05_16-23-43_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_16-30-43_False_0.csv, day_log_12-05_16-30-43_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-31-22_False_0.csv, day_log_12-05_16-31-22_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_16-32-54_False_0.csv, day_log_12-05_16-32-54_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_16-39-05_False_5.csv, day_log_12-05_16-39-05_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_16-39-51_False_0.csv, day_log_12-05_16-39-51_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-41-26_False_5.csv, day_log_12-05_16-41-26_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_16-47-10_False_100.csv, day_log_12-05_16-47-10_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_16-48-58_False_0.csv, day_log_12-05_16-48-58_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-49-55_False_100.csv, day_log_12-05_16-49-55_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_16-55-33_True_0.csv, day_log_12-05_16-55-33_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_16-57-45_False_0.csv, day_log_12-05_16-57-45_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_16-58-32_True_0.csv, day_log_12-05_16-58-32_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_17-05-10_True_5.csv, day_log_12-05_17-05-10_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_17-07-12_False_0.csv, day_log_12-05_17-07-12_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_17-08-18_True_5.csv, day_log_12-05_17-08-18_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_17-15-09_True_100.csv, day_log_12-05_17-15-09_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_17-16-26_False_0.csv, day_log_12-05_17-16-26_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_17-18-00_True_100.csv, day_log_12-05_17-18-00_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_17-24-46_False_0.csv, day_log_12-05_17-24-46_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_17-25-35_False_0.csv, day_log_12-05_17-25-35_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_17-27-50_False_0.csv, day_log_12-05_17-27-50_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_17-33-29_False_5.csv, day_log_12-05_17-33-29_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_17-34-49_False_0.csv, day_log_12-05_17-34-49_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_17-36-43_False_5.csv, day_log_12-05_17-36-43_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_17-42-17_False_100.csv, day_log_12-05_17-42-17_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_17-44-11_False_0.csv, day_log_12-05_17-44-11_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_17-45-33_False_100.csv, day_log_12-05_17-45-33_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_17-51-11_True_0.csv, day_log_12-05_17-51-11_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_17-53-38_False_0.csv, day_log_12-05_17-53-38_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_17-54-20_True_0.csv, day_log_12-05_17-54-20_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_18-01-03_True_5.csv, day_log_12-05_18-01-03_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_18-03-06_False_0.csv, day_log_12-05_18-03-06_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_18-04-14_True_5.csv, day_log_12-05_18-04-14_True_5.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_18-10-38_True_100.csv, day_log_12-05_18-10-38_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_18-12-10_False_0.csv, day_log_12-05_18-12-10_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_18-13-57_True_100.csv, day_log_12-05_18-13-57_True_100.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_18-19-19_False_0.csv, day_log_12-05_18-19-19_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_18-21-40_False_0.csv, day_log_12-05_18-21-40_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_18-23-45_False_0.csv, day_log_12-05_18-23-45_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_18-27-44_False_5.csv, day_log_12-05_18-27-44_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_18-31-03_False_0.csv, day_log_12-05_18-31-03_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_18-31-35_False_5.csv, day_log_12-05_18-31-35_False_5.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/5', lr=0.001, normalize=True, num_day_resample=5, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 5 --log_subdir test_result/5

day_test_log_full_12-05_18-36-36_False_100.csv, day_log_12-05_18-36-36_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_18-40-08_False_100.csv, day_log_12-05_18-40-08_False_100.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/100', lr=0.001, normalize=True, num_day_resample=100, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0 --num_day_resample 100 --log_subdir test_result/100

day_test_log_full_12-05_18-40-47_False_0.csv, day_log_12-05_18-40-47_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_18-45-30_True_0.csv, day_log_12-05_18-45-30_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_18-48-44_True_0.csv, day_log_12-05_18-48-44_True_0.csv
Namespace(ae=0.645, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/0', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --ae 0.645 --num_day_resample 0 --log_subdir test_result/0

day_test_log_full_12-05_18-50-30_False_0.csv, day_log_12-05_18-50-30_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_18-59-59_False_0.csv, day_log_12-05_18-59-59_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, log_subdir='test_result/4_layers', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=4, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --log_subdir test_result/4_layers --test --num_layers 4

day_test_log_full_12-05_20-14-17.csv, log_12-05_20-14-17.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=0, epoch_days_test=10.0, epochs=10, epochs_warm=5, include_invalid=False, log_subdir='test_result', lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=True, use_kl_div=False, use_last_loss=False, vae=False, warm_epoch_days=30.0)
main.py --cuda --epochs 10 --normalize --log_subdir test_result --test --epoch_days_test 10 --warm_epoch_days 30

