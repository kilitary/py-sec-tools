rule _Free_Pascal_0_99_10_yqfzda
{
	meta:
		description = "Free Pascal 0_99_10"
	strings:
		$a = {E8006E00005589E58B7D0C8B750889F88B5D1029}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
