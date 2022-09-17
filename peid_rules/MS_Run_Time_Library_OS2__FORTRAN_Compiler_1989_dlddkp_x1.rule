rule _MS_Run_Time_Library_OS2__FORTRAN_Compiler_1989_dlddkp
{
	meta:
		description = "MS Run_Time Library _OS2_ _ FORTRAN Compiler 1989"
	strings:
		$a = {B430CD2186E02EA3????3D????73}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
