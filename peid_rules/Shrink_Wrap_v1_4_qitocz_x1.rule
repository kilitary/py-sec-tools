rule _Shrink_Wrap_v1_4_qitocz
{
	meta:
		description = "Shrink Wrap v1_4"
	strings:
		$a = {58608BE85533F6684801????E84901????EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
