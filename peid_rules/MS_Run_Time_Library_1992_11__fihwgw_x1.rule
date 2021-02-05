rule _MS_Run_Time_Library_1992_11__fihwgw
{
	meta:
		description = "MS Run_Time Library 1992 _11_"
	strings:
		$a = {B451CD218EDBB8????83E8??8EC033F633FFB9????FCF3A5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
