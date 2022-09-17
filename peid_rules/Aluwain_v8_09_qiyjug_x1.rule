rule _Aluwain_v8_09_qiyjug
{
	meta:
		description = "Aluwain v8_09"
	strings:
		$a = {8BEC1EE8????9D5E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
