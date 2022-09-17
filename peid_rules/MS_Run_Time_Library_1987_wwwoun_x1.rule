rule _MS_Run_Time_Library_1987_wwwoun
{
	meta:
		description = "MS Run_Time Library 1987"
	strings:
		$a = {B430CD213C0273??9A????????B8????509A????????92}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
