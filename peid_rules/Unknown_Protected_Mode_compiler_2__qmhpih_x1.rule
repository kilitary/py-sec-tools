rule _Unknown_Protected_Mode_compiler_2__qmhpih
{
	meta:
		description = "Unknown Protected Mode compiler _2_"
	strings:
		$a = {FAFC0E1FE8????8CC0660FB7C066C1E0??6667A3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
