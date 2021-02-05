rule _Exe_Locker_1_0__IonIce_eaubpx
{
	meta:
		description = "Exe Locker 1_0 __ IonIce"
	strings:
		$a = {E800000000608B6C242081ED05000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
