<script lang="ts">
	export let type = 'info';
	export let content = '';

	const classNames: Record<string, string> = {
		info: 'bg-blue-500/20 text-blue-900 dark:bg-blue-900/40 dark:text-blue-100',
		success: 'bg-green-600/20 text-green-900 dark:bg-green-900/40 dark:text-green-100',
		warning: 'bg-yellow-500/20 text-yellow-900 dark:bg-yellow-900/40 dark:text-yellow-100',
		error: 'bg-red-500/20 text-red-900 dark:bg-red-900/40 dark:text-red-100',
		muted: 'bg-gray-500/30 text-gray-800 dark:text-gray-100'
	};
</script>

<div
	class=" text-xs font-medium {classNames[type] ??
		classNames['info']} w-fit px-[5px] rounded-lg uppercase line-clamp-1 mr-0.5"
>
	{content}
</div>
