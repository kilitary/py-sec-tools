rule _Aluwain_v8_09_fuwpdk
{
	meta:
		description = "Aluwain v8_09"
	strings:
		$a = {8BEC1EE8????9D5E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
