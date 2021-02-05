rule _Exe_Locker_v1_0___IonIce_daflyf
{
	meta:
		description = "Exe Locker v1_0 ___ IonIce"
	strings:
		$a = {E800000000608B6C242081ED050000003E8F856C0000003E8F85680000003E8F85640000003E8F85600000003E8F855C0000003E8F85580000003E8F85540000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
