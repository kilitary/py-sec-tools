rule _MS_Run_Time_Library_1992_13__xliucf
{
	meta:
		description = "MS Run_Time Library 1992 _13_"
	strings:
		$a = {BF????8EDFFA8ED781C4????FB33DBB8????CD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
