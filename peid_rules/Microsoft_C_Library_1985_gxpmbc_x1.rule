rule _Microsoft_C_Library_1985_gxpmbc
{
	meta:
		description = "Microsoft C Library 1985"
	strings:
		$a = {BF????8B36????2BF781FE????72??BE????FA8ED781C4????FB73}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
