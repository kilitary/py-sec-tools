rule _Thunderbolt_V0_02__deXep_forgot__Sign_By_fly_wyxtll
{
	meta:
		description = "Thunderbolt V0_02 __ deXep _forgot_ _ Sign_By_fly"
	strings:
		$a = {E90000000060E8140000005D81ED000000006A45E8A30000006800000000E85861E8AA000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
