rule _Unknown_Protected_Mode_compiler_1__libumw
{
	meta:
		description = "Unknown Protected Mode compiler _1_"
	strings:
		$a = {FABC????8CC88ED8E8????E8????E8????66B8????????66C1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
