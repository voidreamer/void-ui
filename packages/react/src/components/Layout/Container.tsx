import { forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface ContainerProps extends HTMLAttributes<HTMLDivElement> {
  /** Max width variant */
  size?: 'sm' | 'md' | 'default'
  children?: ReactNode
}

export const Container = forwardRef<HTMLDivElement, ContainerProps>(
  ({ size = 'default', className, children, ...props }, ref) => (
    <div
      ref={ref}
      className={cn('void-container', size !== 'default' && `void-container-${size}`, className)}
      {...props}
    >
      {children}
    </div>
  )
)

Container.displayName = 'Container'
