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

day_test_log_full_12-01_00-15-11_False_1.csv, day_log_12-01_00-15-11_False_1.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --num_day_resample 1

day_test_log_full_12-01_00-18-38_False_0.csv, day_log_12-01_00-18-38_False_0.csv
Namespace(ae=0.0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.00 --normalize

day_test_log_full_12-01_00-22-13_False_0.csv, day_log_12-01_00-22-13_False_0.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --num_day_resample 0

day_test_log_full_12-01_00-25-40_True_0.csv, day_log_12-01_00-25-40_True_0.csv
Namespace(ae=0.04, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=0, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.04 --normalize

day_test_log_full_12-01_00-28-41_True_1.csv, day_log_12-01_00-28-41_True_1.csv
Namespace(ae=0.75, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=1, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --ae 0.75 --normalize --num_day_resample 1

day_test_log_full_12-01_00-29-37_False_3.csv, day_log_12-01_00-29-37_False_3.csv
Namespace(ae=0, batch_size=200, cuda=True, cw_weight=0, data='', epoch_days=10.0, epoch_days_test=0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, normalize=True, num_day_resample=3, num_hidden_units=512, num_layers=2, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, use_kl_div=False, use_last_loss=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --normalize --num_day_resample 3

