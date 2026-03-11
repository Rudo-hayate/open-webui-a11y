type ToastNotificationSettingsInput = {
	toastNotificationDuration?: number;
} | null | undefined;

export class ToastNotificationSettings {
	static readonly DEFAULT_DURATION_SECONDS = 4; // default svelte-sonner
	static readonly MAX_DURATION_SECONDS = 300;

	static getDuration(settings?: ToastNotificationSettingsInput) {
		const durationSeconds = Number(settings?.toastNotificationDuration);

		if (!Number.isFinite(durationSeconds) || durationSeconds <= 0) {
			return this.DEFAULT_DURATION_SECONDS * 1000;
		}

		return Math.min(this.MAX_DURATION_SECONDS, Math.round(durationSeconds)) * 1000;
	}
}
